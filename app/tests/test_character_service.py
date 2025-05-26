import pytest
from app.domain.entities.character_entity import CharacterEntity
from app.domain.services.character_service_interface import CharacterServiceInterface


class FakeCharacterRepository:
    def __init__(self):
        self.characters = {}

    def get_all(self):
        return list(self.characters.values())

    def get_by_id(self, character_id: int):
        return self.characters.get(character_id)

    def add(self, character: CharacterEntity):
        if character.id in self.characters:
            raise ValueError("Character already exists")
        self.characters[character.id] = character
        return character

    def delete(self, character_id: int):
        if character_id not in self.characters:
            raise ValueError("Character not found")
        del self.characters[character_id]


class CharacterService(CharacterServiceInterface):
    def __init__(self, repository):
        self.repository = repository

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, character_id: int):
        return self.repository.get_by_id(character_id)

    def add(self, character):
        return self.repository.add(character)

    def delete(self, character_id: int):
        return self.repository.delete(character_id)


@pytest.fixture
def character():
    return CharacterEntity(
        id=1,
        name="Luke Skywalker",
        height=172,
        mass=77,
        hair_color="blond",
        skin_color="fair",
        eye_color="blue",
        birth_year=1998,
    )


@pytest.fixture
def service():
    repo = FakeCharacterRepository()
    return CharacterService(repo)


def test_add_and_get_character(service, character):
    service.add(character)
    result = service.get_by_id(1)
    assert result == character


def test_prevent_duplicate_id(service, character):
    service.add(character)
    with pytest.raises(ValueError, match="Character already exists"):
        service.add(character)


def test_delete_character(service, character):
    service.add(character)
    service.delete(1)
    assert service.get_by_id(1) is None


def test_delete_nonexistent_character(service):
    with pytest.raises(ValueError, match="Character not found"):
        service.delete(999)
