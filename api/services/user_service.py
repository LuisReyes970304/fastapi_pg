from api.repository.user_repository import UserRepocitory
from api.utils.passhass import PasswordHasher


class UserServices:
    
    def __init__(self):
        self._user_repository = UserRepocitory()
        self._password_hasher = PasswordHasher()
    
    def find_all(self, session):
        return self._user_repository.find_all(session)

    def create(self, user, session):
        user.password = self._password_hasher.generate_hash(user.password)
        return self._user_repository.create(user, session)

    def update(self, id, user, session):
        user_to_update = self._user_repository.find_one(id, session)
        if not user_to_update:
            return None
        return self._user_repository.update(user_to_update, user, session)

    def delete(self, id, session):
        user_to_delete = self._user_repository.find_one(id, session)
        if not user_to_delete:
            return None
        return self._user_repository.delete(user_to_delete, session)
