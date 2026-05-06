from perception.fetchers.usgs_fetcher import USGSFetcher


fetcher = USGSFetcher()

events = fetcher.fetch_events()

print(f"Fetched {len(events)} events")

print(events[0])