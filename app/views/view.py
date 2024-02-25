from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.controllers.controller import CourierController
from app.db import get_db

router = APIRouter()


@router.get("/b_courier")
def get_courier_location(courier_id: int, db: Session = Depends(get_db)):
    courier_controller = CourierController(session=db)
    return courier_controller.get_courier_location(courier_id)


@router.post("/b_courier")
def change_courier_location(
    courier_id: int, new_location: dict, db: Session = Depends(get_db)
):
    courier_controller = CourierController(session=db)
    return courier_controller.change_courier_location(courier_id, new_location)
