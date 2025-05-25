from abc import ABC, abstractmethod
from app.domain.entities.character_entity import CharacterEntity
from typing import List, Optional


class CharacterServiceInterface(ABC):
    @abstractmethod
    def get_all(self) -> List[CharacterEntity]: pass

    @abstractmethod
    def get_by_id(self, character_id: int) -> Optional[CharacterEntity]: pass

    @abstractmethod
    def add(self, character: CharacterEntity) -> CharacterEntity: pass

    @abstractmethod
    def delete(self, character_id: int) -> None: pass
