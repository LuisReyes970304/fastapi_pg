from api.repository.role_repository import RoleRepository

role_repository = RoleRepository()

class RoleServices:
    def find_all(self, session):
        return role_repository.find_all(session)
    
    def find_one(self, id, session):
        return role_repository.find_one(id, session)