from perception.poller import (
    SeismicPoller,
)


poller = SeismicPoller(
    interval_seconds=30
)

poller.run()