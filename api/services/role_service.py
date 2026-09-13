from api.repository.role_repository import RoleRepository

role_repository = RoleRepository()

class RoleServices:
    def find_all(self, session):
        return role_repository.find_all(session)
    
    def find_one(self, session, id):
        return role_repository.find_one(session, id)