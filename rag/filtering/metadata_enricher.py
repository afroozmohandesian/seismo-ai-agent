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

        # -------------------------
        # Marine hierarchy
        # -------------------------

        "marine": [
            "marine",
        ],

        "tsunami": [
            "tsunami",
        ],

        "offshore": [
            "offshore",
        ],

        "underwater": [
            "underwater",
        ],

        # -------------------------
        # Volcanic hierarchy
        # -------------------------

        "volcanic": [
            "volcanic",
        ],

        "magma": [
            "magma",
        ],

        "tremor": [
            "tremor",
        ],

        # -------------------------
        # Seismic hierarchy
        # -------------------------

        "seismic": [
            "seismic",
        ],

        "earthquake": [
            "earthquake",
        ],

        "tectonic": [
            "tectonic",
        ],

        "microseismic": [
            "microseismic",
        ],

        # -------------------------
        # Soil hierarchy
        # -------------------------

        "soil": [
            "soil",
        ],

        "groundwater": [
            "groundwater",
        ],

        "rainfall": [
            "rainfall",
        ],

        "saturation": [
            "saturation",
        ],

        # -------------------------
        # Aftershock hierarchy
        # -------------------------

        "aftershock": [
            "aftershock",
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