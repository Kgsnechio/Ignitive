from sqlalchemy import Column, Integer, String, JSON

from .database import Base

class Shine(Base):
    __tablename__ = "shine"

    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, nullable=True)
    topic = Column(String, nullable=False)
    answers = Column(JSON, nullable=False)

    def __init__(self, id, topic, parent_id=None, answers=[]):
        self.id = id
        self.topic = topic
        self.parent_id = parent_id
        self.answers = answers
