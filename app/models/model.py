import json

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Courier:
    __tablename__ = "b_couriers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    location = Column(String)

    def set_location(self, data: dict):
        self.location = json.dumps(data)

    def get_location(self):
        return json.loads(self.location) if self.location else {}
