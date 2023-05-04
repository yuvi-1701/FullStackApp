from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from myapp.database.db import get_db
from myapp.models.Measurements import MaleMeasurement
from myapp.schemas.schemas import MeasurementCreate, Measurement, WaistRange, CheckMeasurement

router = APIRouter()


# API endpoints
@router.post("/get_measurement/")
def check_data(measurement: CheckMeasurement, db: Session = Depends(get_db)):
    print(measurement)
    db_waist = (
        db.query(MaleMeasurement.waist)
        .filter(
            MaleMeasurement.height == measurement.height,
            MaleMeasurement.weight == measurement.weight,
            MaleMeasurement.age == measurement.age,
        )
        .first()
    )
    if db_waist:
        return JSONResponse(content={"waist": db_waist[0]}, status_code=200)
    else:
        return JSONResponse(content="Measurement Not Found", status_code=404)


@router.post("/set_measurement/", response_model=Measurement)
def create_measurement(measurement: MeasurementCreate, db: Session = Depends(get_db)):
    try:
        db_waist = (
            db.query(MaleMeasurement.waist)
            .filter(
                MaleMeasurement.height == measurement.height,
                MaleMeasurement.weight == measurement.weight,
                MaleMeasurement.age == measurement.age,
            )
            .first()
        )
        if db_waist:
            db.query(MaleMeasurement).filter(
                MaleMeasurement.height == measurement.height,
                MaleMeasurement.weight == measurement.weight,
                MaleMeasurement.age == measurement.age,
            ).update({"waist": measurement.waist})
        else:
            db_measurement = MaleMeasurement(**measurement.dict())
            db.add(db_measurement)

        db.commit()

    except SQLAlchemyError as e:
        db.SessionLocal.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {e}")

    return JSONResponse(content="Measurement Added.", status_code=200)


@router.get("/measurement/")
def check_data(db: Session = Depends(get_db)):
    db_waist = db.query(MaleMeasurement).all()
    return JSONResponse(jsonable_encoder(db_waist))


# Can also add few other functionalities by using below endpoints

"""
@router.get("/measurements/", response_model=List[Measurement])
def get_measurements(waist_min: float, waist_max: float, db: Session = Depends(get_db)):
    import pdb; pdb.set_trace()
    db_measurements = db.query(MaleMeasurement).filter(MaleMeasurement.waist >= waist_min, MaleMeasurement.waist <= waist_max).all()
    if not db_measurements:
        raise HTTPException(status_code=404, detail="No measurements found")

    return jsonable_encoder(db_measurements)
    

@router.get("/measurements/range/", response_model=WaistRange)
def get_waist_range(db: Session = Depends(get_db)):
    db_min_waist = db.query(MaleMeasurement.waist).order_by(MaleMeasurement.waist).first()
    db_max_waist = db.query(MaleMeasurement.waist).order_by(MaleMeasurement.waist.desc()).first()
    return WaistRange(min_waist=db_min_waist[0], max_waist=db_max_waist[0])

"""
