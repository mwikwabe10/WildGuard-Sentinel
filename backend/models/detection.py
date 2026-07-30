from pydantic import BaseModel
from typing import Optional


class Detection(BaseModel):

    filename: str

    category: str

    confidence: float

    latitude: Optional[float] = 0.0

    longitude: Optional[float] = 0.0