from fastapi import APIRouter, Depends, HTTPException
from api.dto.user_dto import UserData, UserDto, UserUpdateDto
from api.services.user_services import UserServices
from api.models.user_model import User
from api.utils.util import get_session
from sqlmodel import Session

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/user_list", response_model=UserData)
async def root(session: Session = Depends(get_session)):
    user_crud = UserServices()
    users = await user_crud.find_all(session)
    return UserData(user_list=users)

@router.post("/create_user")
async def create_user(user: UserDto, session: Session = Depends(get_session)):
    user_crud = UserServices()
    new_user = User(**user.model_dump())
    user_saved = await user_crud.create(new_user, session)
    return {"message": "User created successfully", "user": user_saved}

@router.patch("/update_user/{id}")
async def update_user(id: int, user: UserUpdateDto, session: Session = Depends(get_session)):
    user_crud = UserServices()
    updated_user = user_crud.update(id, user, session)
    if updated_user is None:
        raise HTTPException(status_code=404, detail=f"User with ID '{id}' not found")
    return {"message": "User updated successfully", "user": updated_user}

@router.delete("/delete_user/{id}")
async def delete_user(id: int, session: Session = Depends(get_session)):
    user_crud = UserServices()
    deleted_user = user_crud.delete(id, session)
    if deleted_user is None:
        raise HTTPException(status_code=404, detail=f"User with ID '{id}' not found")
    return {"message": "User deleted successfully", "user": deleted_user}