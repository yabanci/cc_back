from sqlalchemy.orm import Session

from app.models.model import Courier


class CourierController:
    def __init__(self, session: Session):
        self.session = session

    def get_courier_location(self, courier_id: int) -> dict | None:
        courier = self.session.query(Courier).filter(Courier.id == courier_id).first()
        if courier:
            return courier.get_location()
        return None

    def change_courier_location(self, courier_id: int, new_location: dict) -> dict | None:
        courier = self.session.query(Courier).filter(Courier.id == courier_id).first()
        if courier:
            courier.set_location(new_location)
            self.session.commit()
            return courier.get_location()
        return None
