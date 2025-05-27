from sqlalchemy import Column, Integer, Float, String, create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# Se define la clase base para declarar los modelos ORM
Base = declarative_base()

# Modelo de base de datos que representa la tabla 'characters'.
# Esta clase está ligada al ORM (SQLAlchemy) y se utiliza únicamente en la capa de infraestructura.
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

# Configuración del motor de base de datos SQLite local
DATABASE_URL = "sqlite:///./characters.sqlite3"

# Se crea el motor y la sesión para conectarse a la base de datos
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Función que inicializa las tablas de la base de datos si no existen
def init_db():
    Base.metadata.create_all(bind=engine)