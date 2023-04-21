from sqlalchemy import Column, Float, Integer
from myapp.database.base import Base

class MaleMeasurement(Base):
    __tablename__ = "male_measurements"
    id = Column(Integer, primary_key=True, index=True)
    height = Column(Float, nullable=False)
    age = Column(Float, nullable=False)
    weight = Column(Float, nullable=False)
    waist = Column(Float, nullable=False)

    class Config:
        orm_mode = True
