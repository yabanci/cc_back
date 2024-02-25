from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.model import Courier


def create_courier(db: Session, name: str, location: dict):
    courier = Courier(name=name, location=location)
    db.add(courier)
    db.commit()
    return {"message": "Courier created successfully"}


def get_courier_location(db: Session, courier_id: int):
    courier = db.query(Courier).filter(Courier.id == courier_id).first()
    if courier:
        return courier.location
    raise HTTPException(status_code=404, detail="Courier not found")


def change_courier_location(db: Session, courier_id: int, new_location: dict):
    courier = db.query(Courier).filter(Courier.id == courier_id).first()
    if courier:
        courier.location = new_location
        db.commit()
        return {"message": "Location updated successfully"}
    raise HTTPException(status_code=404, detail="Courier not found")
