from belief.updates.kalman_update import (
    KalmanUpdater,
)

from belief.updates.bayesian_update import (
    BayesianUpdater,
)

from belief.updates.saturation_update import (
    SaturationUpdater,
)

from belief.tracking.reliability_tracker import (
    ReliabilityTracker,
)


class BeliefManager:

    def __init__(
        self,
        store,
    ):

        self.store = store

        self.kalman_updater = (
            KalmanUpdater()
        )

        self.bayesian_updater = (
            BayesianUpdater()
        )

    def process_observation(
        self,
        index,
        prior_mean,
        prior_variance,
        observation,
        observation_variance,
        soil_saturation,
        process_noise=0.1,
    ):

        predicted_mean, predicted_variance = (
            self.kalman_updater.update(
                prior_mean,
                prior_variance,
                observation,
                observation_variance,
            )
        )

        posterior_mean, posterior_variance = (
            self.bayesian_updater.update(
                prior_mean=predicted_mean,
                prior_variance=predicted_variance,
                observation=observation,
                observation_variance=observation_variance,
            )
        )

        adjusted_vs = (
            SaturationUpdater.apply(
                base_vs=posterior_mean,
                soil_saturation=soil_saturation,
            )
        )

        confidence = (
            ReliabilityTracker.compute_confidence(
                posterior_variance
            )
        )

        self.store.update_cell(
            index=index,
            mean_vs=adjusted_vs,
            variance_vs=posterior_variance,
            soil_saturation=soil_saturation,
            confidence=confidence,
        )

        return self.store.get_cell(
            index
        )