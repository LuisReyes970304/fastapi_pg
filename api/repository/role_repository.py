from api.models.role_model import Role
from sqlmodel import select, Session


class RoleRepository:
    
    def find_all(self, session):
        statement = select(Role)
        return session.exec(statement).all()
    
    def find_one(self, id, session):
            statement = select(Role).where(Role.id == id)
            return session.exec(statement).one_or_none()