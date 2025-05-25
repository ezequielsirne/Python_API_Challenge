from pydantic import BaseModel, Field


class CharacterEntity(BaseModel):
    id: int
    name: str
    height: float
    mass: float
    hair_color: str
    skin_color: str
    eye_color: str
    birth_year: int
    