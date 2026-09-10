from fastapi import APIRouter, Depends
from api.dto.user_dto import UserData, UserDto
from api.repository.user_repository import UserCrud
from api.models.user_model import User
from api.utils.util import get_session
from sqlmodel import Session

router = APIRouter()

@router.get("/user_list", response_model=UserData)
async def root(session: Session = Depends(get_session)):
    user_crud = UserCrud()
    users = [user.model_dump() async for user in user_crud.find_all(User, session)]
    return UserData(users=users)

@router.post("/create_user")
async def create_user(user: UserDto, session: Session = Depends(get_session)):
    user_crud = UserCrud()
    new_user = User(**user.model_dump())
    user_saved = user_crud.create(new_user, session)
    return {"message": "User created successfully", "user": user_saved}