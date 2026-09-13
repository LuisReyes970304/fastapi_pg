from api.models.user_model import User
from sqlmodel import select

class UserRepocitory:

    def find_all(self, session):
        statement = select(User).where(User.is_active == True)
        return session.exec(statement).all()

    def find_one(self, id, session):
        statement = select(User).where(User.id == id)
        return session.exec(statement).one_or_none()

    def create(self, user, session):
        session.add(user)
        session.commit()
        session.refresh(user)
        return user

    def update(self, result, user, session):
        for key, value in user.model_dump(exclude_unset=True).items():
            setattr(result, key, value)
        session.add(result)
        session.commit()
        session.refresh(result)
        return result

    def delete(self, result, session):
        session.delete(result)
        session.commit()
        return result
