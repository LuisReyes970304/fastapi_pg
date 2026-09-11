from fastapi import APIRouter, Depends, HTTPException
from api.dto.user_dto import UserData, UserDto, UserUpdateDto
from api.repository.user_repository import UserRepository
from api.models.user_model import User
from api.utils.util import get_session
from sqlmodel import Session
from typing import Annotated

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/user_list", response_model=UserData)
async def root(session: Session = Depends(get_session)):
    user_crud = UserRepository()
    users = [user.model_dump() async for user in user_crud.find_all(User, session)]
    return UserData(users=users)

@router.post("/create_user")
async def create_user(user: UserDto, session: Session = Depends(get_session)):
    user_crud = UserRepository()
    new_user = User(**user.model_dump())
    user_saved = await user_crud.create(new_user, session)
    return {"message": "User created successfully", "user": user_saved}

@router.patch("/update_user/{email}")
async def update_user(email: str, user: UserUpdateDto, session: Session = Depends(get_session)):
    user_crud = UserRepository()
    updated_user = user_crud.update(email, user, session)
    if updated_user is None:
        raise HTTPException(status_code=404, detail=f"User with email '{email}' not found")
    return {"message": "User updated successfully", "user": updated_user}

@router.delete("/delete_user/{email}")
async def delete_user(email: str, session: Session = Depends(get_session)):
    user_crud = UserRepository()
    deleted_user = user_crud.delete(email, session)
    if deleted_user is None:
        raise HTTPException(status_code=404, detail=f"User with email '{email}' not found")
    return {"message": "User deleted successfully", "user": deleted_user}