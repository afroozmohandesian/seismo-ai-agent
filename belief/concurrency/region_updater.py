class RegionUpdater:

    def __init__(
        self,
        belief_store,
        updater,
    ):

        self.belief_store = belief_store

        self.updater = updater

    def update_region(
        self,
        indices,
        observations,
        observation_variance,
    ):

        for index, observed_vs in zip(
            indices,
            observations,
        ):

            current_state = (
                self.belief_store.read(index)
            )

            updated_mean, updated_variance = (
               self.updater.update(
                    float(
                        current_state["mean_vs"]
                    ),
                    float(
                        current_state["variance_vs"]
                    ),
                    observed_vs,
                    observation_variance,
                )
            )

            confidence = 1.0 / (
                1.0 + updated_variance
            )

            updated_state = {
                "mean_vs": updated_mean,
                "variance_vs": updated_variance,
                "soil_saturation": float(
                    current_state[
                        "soil_saturation"
                    ]
                ),
                "confidence": confidence,
            }

            self.belief_store.write(
                index,
                updated_state,
            )

        self.belief_store.flush()