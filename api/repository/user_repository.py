from api.models.user_model import User
from sqlmodel import select

class UserRepocitory:
    
    async def find_all(self, session):
        statement = select(User).where(User.is_active == True)
        return session.exec(statement).all()

    async def find_one(self, id, session):
        statement = select(User).where(User.id == id)
        result = session.exec(statement).one_or_none()
        return result

    async def create(self, user, session):
        session.add(user)
        self.refresh(user, session)
        return user

    def update(self, result, user, session):
        for key, value in user.model_dump(exclude_unset=True).items():
            setattr(result, key, value)
        session.add(result)
        self.refresh(result, session)
        return result

    def delete(self, result, session):
        if not result:
            return None
        session.delete(result)
        self.refresh(result, session)
        return result
    
    def refresh(self, result, session):
        if(result == None):
            return session.commit()
        session.commit()
        session.refresh(result)
        return result
