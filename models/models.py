from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session
from .database import Base, engine, SessionLocal

# Definição da model
class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    def __repr__(self):
        return f"Usuario(id={self.id}, nome={self.nome}, email={self.email})"
    
    def __init__(self, **kw):
        super().__init__(**kw)

    @classmethod
    def create(cls, nome: str, email: str):
        with SessionLocal() as db:
            novo_usuario = cls(nome=nome, email=email)
            db.add(novo_usuario)
            db.commit()

    @classmethod
    def get_all(cls):
        with SessionLocal() as db:
            return db.query(cls).all()
        
    @classmethod
    def update_by_id(cls, user_id: int, novo_nome: str = None, novo_email: str = None):
        with SessionLocal() as db:
            usuario = db.query(cls).filter(cls.id == user_id).first()
            if usuario:
                usuario.nome = novo_nome if novo_nome else usuario.nome
                usuario.email = novo_email if novo_email else usuario.email
                db.commit()

    @classmethod
    def delete_by_id(cls,user_id: int):
        with SessionLocal() as db:
            usuario = db.query(cls).filter(cls.id == user_id).first()
            if usuario:
                db.delete(usuario)
                db.commit()
