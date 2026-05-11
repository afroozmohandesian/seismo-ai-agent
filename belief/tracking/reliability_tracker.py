class ReliabilityTracker:

    @staticmethod
    def compute_confidence(
        variance,
    ):

        return 1.0 / (
            1.0 + variance
        )