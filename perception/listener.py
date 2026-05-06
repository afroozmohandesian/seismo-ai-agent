from perception.fetchers.usgs_fetcher import USGSFetcher
from perception.fetchers.emsc_fetcher import EMSCFetcher


class SeismicListener:

    def __init__(self):

        self.primary_fetcher = USGSFetcher()

        self.fallback_fetcher = EMSCFetcher()

    def fetch_events(self):

        try:

            print("Fetching from USGS...")

            return self.primary_fetcher.fetch_events()

        except Exception as exc:

            print(f"USGS failed: {exc}")

            print("Switching to EMSC fallback...")

            return self.fallback_fetcher.fetch_events()