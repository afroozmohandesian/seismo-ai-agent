class HierarchicalFilter:

    CATEGORY_HIERARCHY = {

        "hazard": [
            "seismic",
            "marine",
            "volcanic",
            "soil",
            "aftershock",
        ],

        "marine": [
            "tsunami",
            "offshore",
            "underwater",
        ],

        "volcanic": [
            "magma",
            "tremor",
        ],

        "seismic": [
            "earthquake",
            "tectonic",
            "microseismic",
        ],
    }

    @classmethod
    def expand_category(
        cls,
        category,
    ):

        expanded = [category]

        children = cls.CATEGORY_HIERARCHY.get(
            category,
            []
        )

        expanded.extend(children)

        return expanded