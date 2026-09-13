from api.repository.user_repository import UserRepocitory
from api.utils.passhass import PasswordHasher

user_repository = UserRepocitory()
password_hasher = PasswordHasher()

class UserServices:
    def find_all(self, session):
        return user_repository.find_all(session)

    def create(self, user, session):
        user.password = password_hasher.generate_hash(user.password)
        return user_repository.create(user, session)

    def update(self, id, user, session):
        user_to_update = user_repository.find_one(id, session)
        if not user_to_update:
            return None
        return user_repository.update(user_to_update, user, session)

    def delete(self, id, session):
        user_to_delete = user_repository.find_one(id, session)
        if not user_to_delete:
            return None
        return user_repository.delete(user_to_delete, session)
