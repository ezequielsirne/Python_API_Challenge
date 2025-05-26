from sqlalchemy import Column, Integer, Float, String, create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# Declarative base
Base = declarative_base()

# Entidad ORM
class CharacterDB(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    height = Column(Float, nullable=False)
    mass = Column(Float, nullable=False)
    hair_color = Column(String, nullable=False)
    skin_color = Column(String, nullable=False)
    eye_color = Column(String, nullable=False)
    birth_year = Column(Integer, nullable=False)


# Base de datos SQLite
DATABASE_URL = "sqlite:///./characters.sqlite3"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Crear tablas si no existen
def init_db():
    Base.metadata.create_all(bind=engine)