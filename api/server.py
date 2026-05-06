from fastapi import FastAPI

from perception.storage.sqlite_store import (
    SQLiteStore,
)
from api.schemas import (
    EventsResponse,
)

app = FastAPI(
    title="Seismo AI Agent",
    version="0.1.0",
)


store = SQLiteStore()


@app.get("/health")
def health_check():

    return {
        "status": "ok"
    }


@app.get(
    "/events",
    response_model=EventsResponse,
)
def get_events():

    events = (
        store.fetch_existing_events()
    )

    return {
    "count": len(events),

    "events": [

        {
            "eid": event.eid,
            "timestamp": (
                event.timestamp.isoformat()
            ),
            "lat": event.lat,
            "lon": event.lon,
            "depth": event.depth,
            "Mw": event.Mw,
        }

        for event in events
    ],
}