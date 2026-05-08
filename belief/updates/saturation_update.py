class SaturationUpdater:

    @staticmethod
    def apply(
        base_vs,
        soil_saturation,
        alpha=0.5,
    ):

        adjusted_vs = (
            base_vs
            +
            alpha * soil_saturation
        )

        return adjusted_vs