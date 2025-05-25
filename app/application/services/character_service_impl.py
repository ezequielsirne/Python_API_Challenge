from app.domain.entities.character_entity import CharacterEntity
from app.domain.services.character_service_interface import CharacterServiceInterface
from app.application.repositories.character_repository import CharacterRepository
from typing import List, Optional


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
