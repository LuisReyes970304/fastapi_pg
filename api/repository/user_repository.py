from sqlmodel import select
from api.models.user_model import User


class UserRepository:
    async def find_all(self, user, session):
            statement = select(user)
            results = session.exec(statement)
            for user in results:
                yield user
                
    async def create(self, user, session):
            session.add(user)
            session.commit()
            session.refresh(user)
            session.close()
            return user
        
    def update(self, email, user, session):
        statement = select(User).where(User.email == email)
        user_to_update = session.exec(statement).one_or_none()
        if not user_to_update:
            return None
        for key, value in user.model_dump(exclude_unset=True).items():
            setattr(user_to_update, key, value)

        session.add(user_to_update)
        session.commit()
        session.refresh(user_to_update)

        return user_to_update
    
    def delete(self, email, session):
        statement = select(User).where(User.email == email)
        user_to_delete = session.exec(statement).one_or_none()
        if not user_to_delete:
            return None
        session.delete(user_to_delete)
        session.commit()
        return user_to_delete
    
    