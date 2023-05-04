from pydantic import BaseModel

# Pydantic models
class MeasurementCreate(BaseModel):
    height: float
    age: float
    weight: float
    waist: float


class Measurement(BaseModel):
    height: float
    age: float
    weight: float
    waist: float
    id: int


class WaistRange(BaseModel):
    min_waist: float
    max_waist: float


class CheckMeasurement(BaseModel):
    height: float
    age: float
    weight: float
