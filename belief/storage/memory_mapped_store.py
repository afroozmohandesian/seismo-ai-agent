import numpy as np


class MemoryMappedBeliefStore:

    def __init__(
        self,
        path,
        shape,
    ):

        self.dtype = np.dtype(
            [
                ("mean_vs", np.float32),
                ("variance_vs", np.float32),
                ("soil_saturation", np.float32),
                ("confidence", np.float32),
            ]
        )

        self.store = np.memmap(
            path,
            dtype=self.dtype,
            mode="w+",
            shape=shape,
        )

    def write(
        self,
        index,
        belief_state,
    ):

        self.store[index] = (
            belief_state["mean_vs"],
            belief_state["variance_vs"],
            belief_state["soil_saturation"],
            belief_state["confidence"],
        )

    def read(
        self,
        index,
    ):

        return self.store[index]

    def flush(self):

        self.store.flush()