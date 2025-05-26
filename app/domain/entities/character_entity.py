from pydantic import BaseModel, Field


class CharacterEntity(BaseModel):
    id: int = Field(..., strict=True)
    name: str
    height: float = Field(..., strict=True)
    mass: float = Field(..., strict=True)
    hair_color: str
    skin_color: str
    eye_color: str
    birth_year: int = Field(..., strict=True)
    