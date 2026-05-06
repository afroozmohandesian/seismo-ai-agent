from pydantic import BaseModel


class EventResponse(BaseModel):

    eid: str

    timestamp: str

    lat: float
    lon: float

    depth: float

    Mw: float


class EventsResponse(BaseModel):

    count: int

    events: list[EventResponse]