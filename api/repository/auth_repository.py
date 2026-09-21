from api.models.user_model import User
from sqlmodel import select

class AuthRepository:

    def find_one(self, email, session):
        statement = select(User).where(User.email == email)
        return session.exec(statement).one_or_none()