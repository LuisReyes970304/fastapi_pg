from fastapi import APIRouter
from api.repository.user_repository import UserCrud
from api.dto.user_dto import UserDto


router = APIRouter()

@router.post("/create_user")
async def create_user(user: UserDto):
    return {"message": "User created successfully", "user": user}
    # new_user = UserCrud()
    # return new_user.create(user)



