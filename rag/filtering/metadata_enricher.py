class MetadataEnricher:

    REGIONS = [
        "Sicily",
        "Greece",
        "Turkey",
        "Italy",
        "Aegean",
        "Spain",
        "Portugal",
        "Morocco",
        "Tunisia",
        "Algeria",
    ]

    CATEGORY_KEYWORDS = {
        "marine": [
            "marine",
            "underwater",
            "offshore",
            "tsunami",
        ],

        "volcanic": [
            "volcanic",
            "magma",
            "tremor",
        ],

        "aftershock": [
            "aftershock",
        ],

        "soil": [
            "soil",
            "groundwater",
            "rainfall",
            "saturation",
        ],

        "seismic": [
            "earthquake",
            "tectonic",
            "seismic",
        ],
    }

    SOURCE_KEYWORDS = {
        "USGS": ["USGS"],
        "EMSC": ["EMSC"],
    }

    @classmethod
    def enrich(cls, text):

        metadata = {
            "text": text,
            "region": None,
            "category": None,
            "source": None,
        }

        lower_text = text.lower()

        # -------------------------
        # Region detection
        # -------------------------

        for region in cls.REGIONS:

            if region.lower() in lower_text:

                metadata["region"] = region
                break

        # -------------------------
        # Category detection
        # -------------------------

        for category, keywords in (
            cls.CATEGORY_KEYWORDS.items()
        ):

            matched = False

            for keyword in keywords:

                if keyword in lower_text:

                    metadata["category"] = category
                    matched = True
                    break

            if matched:
                break
        # -------------------------
        # Source detection
        # -------------------------

        for source, keywords in (
            cls.SOURCE_KEYWORDS.items()
        ):

            for keyword in keywords:

                if keyword.lower() in lower_text:

                    metadata["source"] = source
                    break

        return metadata