from fastapi import APIRouter
from api.dto.user_dto import UserDto
router = APIRouter()


@router.patch("/update_user")
async def update_user(id_to_update, user_change:UserDto):
    return
#     for user in fake_db:
#         if int(id_to_update) == int(user["user_id"]):
#             updated = await update_user_data(user, user_change)
#             with open(document, "w") as file:
#                 json.dump(fake_db, file, indent=4)
#             return updated


# async def update_user_data(user, user_change):
#     user["name"] = user_change.name
#     user["email"] = user_change.email
#     user["password"] = user_change.password
#     return user_change

