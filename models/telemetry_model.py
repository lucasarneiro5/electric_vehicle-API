from pydantic import BaseModel
from datetime import datetime


class GPS(BaseModel):
    latitude: float
    longitude: float


class Telemetry(BaseModel):
    bateria: int
    velocidade: float
    gps: GPS
    data_hora: datetime