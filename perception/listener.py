from perception.fetchers.usgs_fetcher import USGSFetcher
from perception.fetchers.emsc_fetcher import EMSCFetcher
from perception.storage.sqlite_store import SQLiteStore

class SeismicListener:

    def __init__(self):

        self.primary_fetcher = USGSFetcher()

        self.fallback_fetcher = EMSCFetcher()

        self.store = SQLiteStore()

    def fetch_events(self):

        try:

            print("Fetching from USGS...")

            events = self.primary_fetcher.fetch_events()

            for event in events:
                self.store.save_event(event)
            return events

        except Exception as exc:

            print(f"USGS failed: {exc}")

            print("Switching to EMSC fallback...")

            events = self.fallback_fetcher.fetch_events()

            for event in events:
                self.store.save_event(event)
            
            return events   