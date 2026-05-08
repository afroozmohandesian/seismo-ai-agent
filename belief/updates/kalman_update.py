class KalmanUpdater:

    @staticmethod
    def predict(
        current_mean,
        current_variance,
        process_noise,
    ):

        predicted_mean = current_mean

        predicted_variance = (
            current_variance
            +
            process_noise
        )

        return (
            predicted_mean,
            predicted_variance,
        )