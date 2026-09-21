from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from api.dto.user_dto import UserData, UserDto, UserUpdateDto
from api.models.user_model import User
from api.services.user_service import UserServices

user_services = UserServices()

class UserController:
    def list_users(self, session) -> UserData:
        user_list = user_services.find_all(session)
        return UserData(user_list=[user.model_dump() for user in user_list])

    def create_user(self, user: UserDto, session) -> dict:
        new_user = User(**user.model_dump())
        try:
            created_user = user_services.create(new_user, session)
        except IntegrityError:
            session.rollback()
            raise HTTPException(status_code=409, detail=f"A user with email '{user.email}' already exists")
        return {"message": "User created successfully", "user": created_user.model_dump()}

    def update_user(self, id: int, user: UserUpdateDto, session):
        if not user.model_dump(exclude_unset=True):
            raise HTTPException(status_code=400, detail="No fields provided to update")
        try:
            updated_user = user_services.update(id, user, session)
        except IntegrityError:
            session.rollback()
            raise HTTPException(status_code=409, detail=f"A user with email '{user.email}' already exists")
        if updated_user is None:
            raise HTTPException(status_code=404, detail=f"User with ID '{id}' not found")
        return {"message": "User updated successfully", "user": updated_user.model_dump()}

    def delete_user(self, id: int, session):
        deleted_user = user_services.delete(id, session)
        if deleted_user is None:
            raise HTTPException(status_code=404, detail=f"User with ID '{id}' not found")
        return {"message": "User deleted successfully", "user": deleted_user.model_dump()}
