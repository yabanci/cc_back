import json

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Courier(Base):
    __tablename__ = "b_couriers"

    def __init__(self, name: str, location: dict) -> None:
        self.name = name
        self.location = json.dumps(location)

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    location = Column(String)

    def set_location(self, data: dict):
        self.location = json.dumps(data)

    def get_location(self):
        return json.loads(self.location) if self.location else {}
