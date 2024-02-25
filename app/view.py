from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import controller
from app.db import get_db

router = APIRouter()


@router.post("")
def create_courier(name: str, location: dict, db: Session = Depends(get_db)):
    return controller.create_courier(db, name, location)


@router.get("")
def get_courier_location(courier_id: int, db: Session = Depends(get_db)):
    return controller.get_courier_location(db, courier_id)


@router.post("/{courier_id}/location")
def change_courier_location(
    courier_id: int, new_location: dict, db: Session = Depends(get_db)
):
    return controller.change_courier_location(db, courier_id, new_location)
