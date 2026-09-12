from sqlmodel import select
from api.models.user_model import User
from api.repository.user_repository import UserRepocitory

user_repository = UserRepocitory()

class UserServices:
    async def find_all(self, session):
        user_list = await user_repository.find_all(session)
        return [user.model_dump() for user in user_list]

                
    async def create(self, user, session):
            return user_repository.create(user, session)
        
    def update(self, statement, user, session):
        user_to_update = user_repository.find_one(statement, session)
        if not user_to_update:
            return None
        return user_repository.update(user_to_update, user, session)
    
    def delete(self, statement, session):
        user_to_delete = user_repository.find_one(statement, session)
        if not user_to_delete:
            return None
        return user_repository.delete(user_to_delete, session)

    