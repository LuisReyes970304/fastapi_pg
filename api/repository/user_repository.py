from sqlmodel import select
from api.models.user_model import User


class UserCrud:
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
        
    async def update(self, email, user, session):
            statement = select(User).where(User.email == email)
            results = session.exec(statement)
            user_to_update = results.one_or_none()
            if user_to_update: 
                for key, value in user.model_dump(exclude_unset=True).items():
                    setattr(user_to_update, key, value)
                session.add(user_to_update)
                session.commit()
                session.refresh(user_to_update)
                session.close()
                return user_to_update
            else:
                return None