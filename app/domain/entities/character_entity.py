from pydantic import BaseModel, Field


class CharacterEntity(BaseModel):
    id: int = Field(..., strict=True)
    height: float = Field(..., strict=True)
    mass: float = Field(..., strict=True)
    birth_year: int = Field(..., strict=True)
    name: str
    hair_color: str
    skin_color: str
    eye_color: str
    