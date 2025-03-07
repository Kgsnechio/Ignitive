from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# Definição da Base para os modelos
class Base(DeclarativeBase):
    pass

# URL do banco de dados SQLite
DATABASE_URL = "sqlite:///data/ignitive.db"

# Criar o engine para conexão com o banco
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Criar uma fábrica de sessões
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
