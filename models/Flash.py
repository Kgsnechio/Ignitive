from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from .database import Base

class Flash(Base):
    __tablename__ = "flash"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    shine_id = Column(Integer, ForeignKey("shine.id"), nullable=False)
    question = Column(Integer, nullable=False)
    difficulty = Column(Integer, default=0)  # 0 (fácil) a 3 (muito difícil)

    def __init__(self, shine_id, question, answer):
        self.shine_id = shine_id
        self.question = question
        self.answer = answer
        self.difficulty = 0  # Começa como fácil

    def update_difficulty(self, level):
        """Atualiza a dificuldade do flashcard"""
        self.difficulty = level