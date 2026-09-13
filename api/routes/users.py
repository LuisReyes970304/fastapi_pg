from fastapi import APIRouter, Depends
from api.dto.user_dto import UserData, UserDto, UserUpdateDto
from api.controller.user_controller import UserController
from api.utils.session_util import get_session
from sqlmodel import Session

router = APIRouter(prefix="/users", tags=["Users"])
user_controller = UserController()

@router.get("/user_list", response_model=UserData)
async def get_users(session: Session = Depends(get_session)):
    return user_controller.list_users(session)

@router.post("/create_user")
async def create_user(user: UserDto, session: Session = Depends(get_session)):
    return user_controller.create_user(user, session)

@router.patch("/update_user/{id}")
async def update_user(id: int, user: UserUpdateDto, session: Session = Depends(get_session)):
    return user_controller.update_user(id, user, session)

@router.delete("/delete_user/{id}")
async def delete_user(id: int, session: Session = Depends(get_session)):
    return user_controller.delete_user(id, session)
