from belief.updates.base_updater import (
    BaseUpdater,
)


class KalmanUpdater(BaseUpdater):

    def update(
        self,
        prior_mean,
        prior_variance,
        observation,
        observation_variance,
    ):

        kalman_gain = (
            prior_variance
            /
            (
                prior_variance
                +
                observation_variance
            )
        )

        posterior_mean = (
            prior_mean
            +
            kalman_gain
            *
            (
                observation
                -
                prior_mean
            )
        )

        posterior_variance = (
            1
            -
            kalman_gain
        ) * prior_variance

        return (
            posterior_mean,
            posterior_variance,
        )