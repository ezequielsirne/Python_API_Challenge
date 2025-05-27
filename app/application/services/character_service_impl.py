from app.domain.entities.character_entity import CharacterEntity
from app.domain.services.character_service_interface import CharacterServiceInterface
from app.application.repositories.character_repository import CharacterRepository
from typing import List, Optional

# Implementación concreta del servicio CharacterService.
# Esta clase implementa la interfaz definida en domain (CharacterServiceInterface)
# y orquesta las operaciones de negocio delegando en un repositorio inyectado.
# De esta forma, encapsula la lógica sin acoplarse a la tecnología de persistencia.
class CharacterService(CharacterServiceInterface):
    def __init__(self, repository: CharacterRepository):
        self.repository = repository

    def get_all(self) -> List[CharacterEntity]:
        return self.repository.get_all()

    def get_by_id(self, character_id: int) -> Optional[CharacterEntity]:
        return self.repository.get_by_id(character_id)

    def add(self, character: CharacterEntity) -> CharacterEntity:
        return self.repository.add(character)

    def delete(self, character_id: int) -> None:
        self.repository.delete(character_id)
