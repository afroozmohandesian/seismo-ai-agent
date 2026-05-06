import requests

from perception.models.event import SeismicEvent


USGS_API_URL = (
    "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson"
)


class USGSFetcher:

    def fetch_events(self) -> list[SeismicEvent]:

        response = requests.get(USGS_API_URL, timeout=10)

        response.raise_for_status()

        payload = response.json()

        events = []

        for feature in payload["features"]:

            properties = feature["properties"]
            geometry = feature["geometry"]

            coordinates = geometry["coordinates"]

            try:

                event = SeismicEvent(
                    eid=hash(feature["id"]),

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

            except Exception as exc:
                print(f"Failed to parse event: {exc}")

        return events