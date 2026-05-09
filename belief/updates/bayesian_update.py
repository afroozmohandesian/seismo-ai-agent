from belief.updates.base_updater import (
    BaseUpdater,
)


class BayesianUpdater(BaseUpdater):

    def update(
        self,
        prior_mean,
        prior_variance,
        observation,
        observation_variance,
    ):

        posterior_mean = (
            (
                observation_variance
                *
                prior_mean
                +
                prior_variance
                *
                observation
            )
            /
            (
                prior_variance
                +
                observation_variance
            )
        )

        posterior_variance = (
            (
                prior_variance
                *
                observation_variance
            )
            /
            (
                prior_variance
                +
                observation_variance
            )
        )

        return (
            posterior_mean,
            posterior_variance,
        )