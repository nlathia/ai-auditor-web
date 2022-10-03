from typing import List
from datetime import datetime
import json

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, Column, DateTime, String
from sqlalchemy.sql import func
from dataclasses import dataclass
from dataclasses_json import dataclass_json

db = SQLAlchemy()

@dataclass_json
@dataclass
class Example:

    label: int
    prediction: int
    magnitude: float
    text: str

@dataclass_json
@dataclass
class Row:

    # Audit run
    api_name: str
    dataset_name: str
    created: str
    num_samples: int
    num_minutes: float

    # Metrics
    accuracy: float
    f1: float
    precision: float
    recall: float
    mistakes: list[Example]

class AuditResult(db.Model):

    """ Saving audit results lazily as strings """

    __tablename__ = "results"
    id = Column(Integer, primary_key=True)
    created = Column(DateTime(timezone=True), server_default=func.now())
    contents = Column(String(), unique=False)

    def __init__(self, contents: dict):
        self.contents = json.dumps(contents)

    @classmethod
    def get_all(cls):
        rows = [
            Row.from_json(row.contents)
            for row in db.session.query(cls).all()
        ]
        return sorted(
            rows,
            key=lambda x: datetime.strptime(x.created, "%H:%M %d %B %Y"),
            reverse=True,
        )
