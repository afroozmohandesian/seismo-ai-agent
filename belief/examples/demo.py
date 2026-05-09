from belief.storage.tensor_store import (
    TensorStore,
)

from belief.belief_manager import (
    BeliefManager,
)

from belief.storage.memory_mapped_store import (
    MemoryMappedBeliefStore,
)

from belief.updates.region_updater import (
    RegionUpdater,
)

# --------------------------------------------------
# Initialize tensor storage
# --------------------------------------------------

store = TensorStore(
    shape=(10, 10, 5)
)

# --------------------------------------------------
# Initialize belief manager
# --------------------------------------------------

manager = BeliefManager(
    store=store
)

# --------------------------------------------------
# Initial state
# --------------------------------------------------

prior_mean = 2.5

prior_variance = 0.4

soil_saturation = 0.7

observation = 2.9

observation_variance = 0.2

print("\nProcessing Observation")
print("-" * 50)

result = manager.process_observation(
    index=(1, 2, 3),
    prior_mean=prior_mean,
    prior_variance=prior_variance,
    observation=observation,
    observation_variance=observation_variance,
    soil_saturation=soil_saturation,
)

print(f"Updated Vs mean: {result['mean_vs']}")

print(
    f"Updated uncertainty: "
    f"{result['variance_vs']}"
)

print(
    f"Soil saturation: "
    f"{result['soil_saturation']}"
)

print(
    f"Belief confidence: "
    f"{result['confidence']}"
)

# --------------------------------------------------
# Memory-Mapped Storage
# --------------------------------------------------

print("\n")
print("Memory-Mapped Storage")
print("-" * 50)

mapped_store = (
    MemoryMappedBeliefStore(
        path="belief_state.dat",
        shape=(10, 10),
    )
)

mapped_store.write(
    (0, 0),
    result,
)

stored_cell = mapped_store.read(
    (0, 0)
)

print(stored_cell)

# --------------------------------------------------
# Regional Concurrent Update
# --------------------------------------------------

print("\n")
print("Regional Concurrent Update")
print("-" * 50)

region_updater = RegionUpdater(
    belief_store=mapped_store,
    updater=manager.kalman_updater,
)

region_updater.update_region(
    indices=[
        (0, 0),
    ],
    observations=[
        3.0,
    ],
    observation_variance=0.2,
)

updated_cell = mapped_store.read(
    (0, 0)
)

print(updated_cell)