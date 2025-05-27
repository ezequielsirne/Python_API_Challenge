from pydantic import BaseModel

# DTO (Data Transfer Object) utilizado para limitar los campos expuestos
# en la respuesta del endpoint GET /character/getAll.
class CharacterListDTO(BaseModel):
    id: int
    name: str
    height: float
    mass: float
    birth_year: int
    eye_color: str
