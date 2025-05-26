from pydantic import BaseModel


class CharacterListDTO(BaseModel):
    id: int
    name: str
    height: float
    mass: float
    birth_year: int
    eye_color: str
