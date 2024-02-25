from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.model import Courier


class CourierController:
    def __init__(self, session: Session):
        self.session = session

    def create_courier(self, name: str, location: dict):
        new_courier = Courier(name=name)
        new_courier.set_location(location)
        self.session.add(new_courier)
        self.session.commit()
        return {"message": "Courier created successfully"}

    def get_courier_location(self, courier_id: int):
        courier = self.session.query(Courier).filter(Courier.id == courier_id).first()
        if courier:
            return courier.get_location()
        raise HTTPException(status_code=404, detail="Courier not found")

    def change_courier_location(self, courier_id: int, new_location: dict):
        courier = self.session.query(Courier).filter(Courier.id == courier_id).first()
        if courier:
            courier.set_location(new_location)
            self.session.commit()
            return {"message": "Location updated successfully"}
        raise HTTPException(status_code=404, detail="Courier not found")
