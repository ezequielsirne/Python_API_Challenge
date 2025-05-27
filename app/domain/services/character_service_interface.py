from abc import ABC, abstractmethod
from app.domain.entities.character_entity import CharacterEntity
from typing import List, Optional

# Esta clase representa una interfaz definida como clase abstracta.
# Sirve para declarar las operaciones de negocio que debe ofrecer el servicio
# sin depender de una implementación específica. Permite mantener la lógica
# de negocio limpia y visible dentro de la capa domain.
class CharacterServiceInterface(ABC):
    @abstractmethod
    def get_all(self) -> List[CharacterEntity]: pass

    @abstractmethod
    def get_by_id(self, character_id: int) -> Optional[CharacterEntity]: pass

    @abstractmethod
    def add(self, character: CharacterEntity) -> CharacterEntity: pass

    @abstractmethod
    def delete(self, character_id: int) -> None: pass
