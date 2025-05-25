from abc import ABC, abstractmethod
from app.domain.entities.character_entity import CharacterEntity
from typing import List, Optional


class CharacterRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[CharacterEntity]:
        """Obtener todos los personajes"""
        pass

    @abstractmethod
    def get_by_id(self, character_id: int) -> Optional[CharacterEntity]:
        """Obtener un personaje por ID"""
        pass

    @abstractmethod
    def add(self, character: CharacterEntity) -> CharacterEntity:
        """Agregar un nuevo personaje"""
        pass

    @abstractmethod
    def delete(self, character_id: int) -> None:
        """Eliminar un personaje por ID"""
        pass