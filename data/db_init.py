from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Definição da Base primeiro
from models import Base, SessionLocal, engine, User, Shine, Flash 

# Criando as tabelas no banco
Base.metadata.create_all(engine)

# Criando sessão
session = SessionLocal()
