import requests

from shared.retry import retry
from perception.models.event import SeismicEvent


EMSC_API_URL = (
    "https://www.seismicportal.eu/fdsnws/event/1/query"
    "?limit=20&format=json"
)


class EMSCFetcher:

    def fetch_events(self) -> list[SeismicEvent]:

        def request():

            response = requests.get(
                EMSC_API_URL,
                timeout=10,
            )

            response.raise_for_status()

            return response.json()

        payload = retry(request)

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

                    Mw=properties.get("mag", 0.0),

                    dist=0.0,
                    azi=0.0,

                    loclat=coordinates[1],
                    loclon=coordinates[0],
                )

                events.append(event)

            except Exception as exc:

                print(f"Failed to parse EMSC event: {exc}")

        return events