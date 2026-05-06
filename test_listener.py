from perception.listener import SeismicListener


listener = SeismicListener()

events = listener.fetch_events()

print(f"Fetched {len(events)} events")