from app.application.repositories.character_repository import CharacterRepository
from app.domain.entities.character_entity import CharacterEntity
from app.infrastructure.database import SessionLocal, CharacterDB
from sqlalchemy.orm import Session
from typing import List, Optional


class SQLAlchemyCharacterRepository(CharacterRepository):
    def __init__(self, db_session: Session):
        self.db = db_session

    def get_all(self) -> List[CharacterEntity]:
        records = self.db.query(CharacterDB).all()
        return [CharacterEntity(**r.__dict__) for r in records]

    def get_by_id(self, character_id: int) -> Optional[CharacterEntity]:
        record = self.db.query(CharacterDB).filter(CharacterDB.id == character_id).first()
        return CharacterEntity(**record.__dict__) if record else None

    def add(self, character: CharacterEntity) -> CharacterEntity:
        existing = self.db.query(CharacterDB).filter(CharacterDB.id == character.id).first()
        if existing:
            raise ValueError(f"Character with ID {character.id} already exists.")

        db_char = CharacterDB(**character.dict())
        self.db.add(db_char)
        self.db.commit()
        return character

    def delete(self, character_id: int) -> None:
        record = self.db.query(CharacterDB).filter(CharacterDB.id == character_id).first()
        if not record:
            raise ValueError(f"Character with ID {character_id} not found.")
        self.db.delete(record)
        self.db.commit()