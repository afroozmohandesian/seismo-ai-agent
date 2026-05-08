import numpy as np


class TensorStore:

    def __init__(self, shape):

        self.mean_grid = np.zeros(
            shape,
            dtype=np.float32,
        )

        self.variance_grid = np.ones(
            shape,
            dtype=np.float32,
        )

        self.soilsat_grid = np.zeros(
            shape,
            dtype=np.float32,
        )

        self.confidence_grid = np.ones(
            shape,
            dtype=np.float32,
        )

    def update_cell(
        self,
        index,
        mean_vs,
        variance_vs,
        soil_saturation,
        confidence,
    ):

        self.mean_grid[index] = mean_vs

        self.variance_grid[index] = variance_vs

        self.soilsat_grid[index] = soil_saturation

        self.confidence_grid[index] = confidence

    def get_cell(
        self,
        index,
    ):

        return {
            "mean_vs": self.mean_grid[index],
            "variance_vs": self.variance_grid[index],
            "soil_saturation": self.soilsat_grid[index],
            "confidence": self.confidence_grid[index],
        }