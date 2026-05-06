from datetime import datetime
from pydantic import BaseModel, Field


class SeismicEvent(BaseModel):
    eid: int
    timestamp: datetime

    lat: float = Field(..., ge=-90, le=90)
    lon: float = Field(..., ge=-180, le=180)

    depth: float = Field(..., ge=-100, le=0)

    Mw: float = Field(..., ge=0, le=9)

    dist: float = Field(..., ge=0)

    azi: float = Field(..., ge=-180, le=180)

    loclat: float = Field(..., ge=-90, le=90)
    loclon: float = Field(..., ge=-180, le=180)