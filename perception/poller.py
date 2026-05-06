import time

from perception.listener import SeismicListener
from shared.logger import logger


class SeismicPoller:

    def __init__(
        self,
        interval_seconds: int = 60,
    ):

        self.interval_seconds = (
            interval_seconds
        )

        self.listener = (
            SeismicListener()
        )

    def run(self):

        logger.info(
            "Starting seismic polling service"
        )

        while True:

            try:

                events = (
                    self.listener.fetch_events()
                )

                logger.info(
                    f"Fetched {len(events)} "
                    f"new events"
                )

            except Exception as exc:

                logger.error(
                    f"Polling cycle failed: "
                    f"{exc}"
                )

            time.sleep(
                self.interval_seconds
            )