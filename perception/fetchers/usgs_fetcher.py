import requests

from shared.retry import retry
from perception.models.event import SeismicEvent

from shared.sync_state import SyncStateManager


USGS_API_URL = (
    "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson"
)


class USGSFetcher:

    def fetch_events(self) -> list[SeismicEvent]:

        def request():

            response = requests.get(
                USGS_API_URL,
                timeout=10,
            )

            response.raise_for_status()

            return response.json()

        payload = retry(request)

        events = []
        state_manager = SyncStateManager()

        last_event_time = (
            state_manager.get_last_event_time()
        )

        latest_seen_time = last_event_time

        for feature in payload["features"]:

            properties = feature["properties"]
            event_time = properties["time"]

            if event_time <= last_event_time:
                continue
            geometry = feature["geometry"]

            coordinates = geometry["coordinates"]

            try:

                event = SeismicEvent(
                    eid=str(feature["id"]),

                    timestamp=properties["time"],

                    lon=coordinates[0],
                    lat=coordinates[1],

                    depth=-abs(coordinates[2]),

                    Mw=properties["mag"] or 0.0,

                    dist=0.0,
                    azi=0.0,

                    loclat=coordinates[1],
                    loclon=coordinates[0],
                )

                events.append(event)
                latest_seen_time = max(
                    latest_seen_time,
                    event_time,
            )

            except Exception as exc:

                print(f"Failed to parse event: {exc}")
        
        state_manager.save_last_event_time(
            latest_seen_time
        )
        return events