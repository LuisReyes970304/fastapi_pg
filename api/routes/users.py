from fastapi import APIRouter, Depends, HTTPException
from api.dto.user_dto import UserData, UserDto, UserUpdateDto
from api.repository.user_repository import UserCrud
from api.models.user_model import User
from api.utils.util import get_session
from sqlmodel import Session
from typing import Annotated

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/user_list", response_model=UserData)
async def root(session: Session = Depends(get_session)):
    user_crud = UserCrud()
    users = [user.model_dump() async for user in user_crud.find_all(User, session)]
    return UserData(users=users)

@router.post("/create_user")
async def create_user(user: UserDto, session: Session = Depends(get_session)):
    user_crud = UserCrud()
    new_user = User(**user.model_dump())
    user_saved = await user_crud.create(new_user, session)
    return {"message": "User created successfully", "user": user_saved}

@router.patch("/update_user/{email}")
async def update_user(email: str, user: UserUpdateDto, session: Session = Depends(get_session)):
    user_crud = UserCrud()
    updated_user = user_crud.update(email, user, session)
    if updated_user is None:
        raise HTTPException(status_code=404, detail=f"User with email '{email}' not found")
    return {"message": "User updated successfully", "user": updated_user}