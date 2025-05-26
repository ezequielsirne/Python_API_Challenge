from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.domain.entities.character_entity import CharacterEntity
from app.domain.dtos.character_list_dto import CharacterListDTO
from app.infrastructure.database import SessionLocal
from app.infrastructure.repositories.character_repository_impl import SQLAlchemyCharacterRepository
from app.application.services.character_service_impl import CharacterService

router = APIRouter(prefix="/character", tags=["Character"])


# Dependency: crear repo + servicio
def get_service():
    db: Session = SessionLocal()
    repo = SQLAlchemyCharacterRepository(db)
    return CharacterService(repo)


@router.get("/getAll", response_model=list[CharacterListDTO])
def get_all_characters(service: CharacterService = Depends(get_service)):
    return service.get_all()


@router.get("/get/{character_id}", response_model=CharacterEntity)
def get_character(character_id: int, service: CharacterService = Depends(get_service)):
    character = service.get_by_id(character_id)
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")
    return character


@router.post("/add", response_model=CharacterEntity)
def add_character(character: CharacterEntity, service: CharacterService = Depends(get_service)):
    try:
        return service.add(character)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/delete/{character_id}")
def delete_character(character_id: int, service: CharacterService = Depends(get_service)):
    try:
        service.delete(character_id)
        return {"detail": "Character deleted successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
