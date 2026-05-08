from pydantic import BaseModel
from typing import Optional


class BeliefCell(BaseModel):

    mean_vs: float

    variance_vs: float

    soil_saturation: float

    confidence: float

    timestamp: Optional[float] = None