class QueryExpander:

    QUERY_EXPANSIONS = {

        "tsunami": [
            "marine hazard",
            "offshore seismic activity",
            "underwater displacement",
        ],

        "earthquake": [
            "tectonic activity",
            "seismic event",
            "aftershock sequence",
        ],

        "volcanic": [
            "magma movement",
            "harmonic tremor",
            "geothermal instability",
        ],

        "USGS": [
            "seismic monitoring",
            "earthquake surveillance",
            "hazard assessment",
        ],

        "EMSC": [
            "seismic alert",
            "tectonic monitoring",
            "hazard notification",
        ],
    }

    @classmethod
    def expand(
        cls,
        query,
    ):

        expanded_terms = [query]

        for keyword, expansions in (
            cls.QUERY_EXPANSIONS.items()
        ):

            if keyword.lower() in query.lower():

                expanded_terms.extend(
                    expansions
                )

        return " ".join(
            expanded_terms
        )