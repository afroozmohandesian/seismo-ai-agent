from belief.storage.tensor_store import (
    TensorStore,
)

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


# --------------------------------------------------
# Initialize tensor storage
# --------------------------------------------------

store = TensorStore(
    shape=(10, 10, 5)
)

# --------------------------------------------------
# Initial belief state
# --------------------------------------------------

prior_mean = 2.5

prior_variance = 0.4

soil_saturation = 0.7

print("\nInitial Belief State")
print("-" * 50)

print(f"Initial Vs mean: {prior_mean}")
print(f"Initial uncertainty: {prior_variance}")

# --------------------------------------------------
# Kalman prediction
# --------------------------------------------------

predicted_mean, predicted_variance = (
    KalmanUpdater.predict(
        current_mean=prior_mean,
        current_variance=prior_variance,
        process_noise=0.1,
    )
)

print("\nPredicted State")
print("-" * 50)

print(f"Predicted mean: {predicted_mean}")
print(
    f"Predicted variance: {predicted_variance}"
)

# --------------------------------------------------
# New observation
# --------------------------------------------------

observation = 2.9

observation_variance = 0.2

print("\nIncoming Observation")
print("-" * 50)

print(f"Observed Vs: {observation}")

# --------------------------------------------------
# Bayesian update
# --------------------------------------------------

posterior_mean, posterior_variance = (
    BayesianUpdater.update(
        prior_mean=predicted_mean,
        prior_variance=predicted_variance,
        observation=observation,
        observation_variance=observation_variance,
    )
)

print("\nPosterior Belief State")
print("-" * 50)

print(f"Updated mean: {posterior_mean}")

print(
    f"Updated variance: {posterior_variance}"
)

# --------------------------------------------------
# Soil saturation adjustment
# --------------------------------------------------

adjusted_vs = (
    SaturationUpdater.apply(
        base_vs=posterior_mean,
        soil_saturation=soil_saturation,
    )
)

print("\nSoil Saturation Adjustment")
print("-" * 50)

print(f"Adjusted Vs: {adjusted_vs}")

# --------------------------------------------------
# Reliability tracking
# --------------------------------------------------

confidence = (
    ReliabilityTracker.compute_confidence(
        posterior_variance
    )
)

print("\nBelief Reliability")
print("-" * 50)

print(f"Confidence: {confidence}")

# --------------------------------------------------
# Store final belief state
# --------------------------------------------------

store.update_cell(
    index=(1, 2, 3),
    mean_vs=adjusted_vs,
    variance_vs=posterior_variance,
    soil_saturation=soil_saturation,
    confidence=confidence,
)

print("\nStored Tensor Cell")
print("-" * 50)

print(
    store.get_cell((1, 2, 3))
)