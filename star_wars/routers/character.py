from typing import Annotated

from sqlalchemy import func
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, Path
from starlette import status
from ..models import Character
from ..database import get_db

router = APIRouter(
    tags=['character']
)
db_dependency = Annotated[Session, Depends(get_db)]


class CharacterRequest(BaseModel):
    name: str = Field(max_length=200)
    height: int = Field(gt=0)
    mass: int = Field(gt=0)
    hair_color: str = Field(max_length=50)
    skin_color: str = Field(max_length=50)
    eye_color: str = Field(max_length=50)
    birth_year: int = Field(gt=0)


@router.get("/character/getAll", status_code=status.HTTP_200_OK)
async def read_all_characters(db: db_dependency):
    """
    Returns all characters stored in the database.

    Response:
    - Status 200 OK: Returns an array containing all characters stored in the database.
      If there are no characters, an empty array [] is returned.
    """
    return db.query(Character).filter().all()


@router.get("/character/get/{character_id}", status_code=status.HTTP_200_OK)
async def read_character(db: db_dependency, character_id: int = Path(gt=0)):
    """
    Returns the character with the specified ID.

    Path Parameters:
    - character_id (int): The ID of the character to retrieve. Must be greater than 0.

    Response:
    - Status 200 OK: Returns the character model with the specified ID.
    - Status 404 Not Found: If the character with the specified ID does not exist.
    """
    character_model = db.query(Character).filter(Character.id == character_id) \
        .filter().first()
    if character_model is not None:
        return character_model
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Character not found.')


@router.post("/character/add", status_code=status.HTTP_201_CREATED)
async def create_character(db: db_dependency,
                           character_request: CharacterRequest):
    """
    Adds a new character to the database.

    Request Body:
    - character_request (CharacterRequest): The details of the character to be added.

    Response:
    - Status 201 Created: If the character is successfully added to the database.
    - Status 400 Bad Request: If a character with the same name already exists in the database.
    """
    existing_character = db.query(Character).filter(
        func.lower(Character.name) == character_request.name.lower()).first()
    if existing_character:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Character with this name already exists")
    character_model = Character(**character_request.dict())
    db.add(character_model)
    db.commit()


@router.delete("/character/delete/{character_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_character( db: db_dependency, character_id: int = Path(gt=0)):
    """
    Deletes the character with the specified ID from the database.

    Path Parameters:
    - character_id (int): The ID of the character to delete. Must be greater than 0.

    Response:
    - Status 204 No Content: If the character is successfully deleted from the database.
    - Status 404 Not Found: If the character with the specified ID does not exist.
    """
    character_model = db.query(Character).filter(Character.id == character_id) \
        .filter().first()
    if character_model is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='character not found.')
    db.query(Character).filter(Character.id == character_id).delete()

    db.commit()
