from api.repository.auth_repository import AuthRepository
from api.utils.passhass import PasswordHasher


class AuthServices:
    def __init__(self):
        self._auth_repository = AuthRepository()
        self._password_hasher = PasswordHasher()
        
    def login(self, email, password, session):
        user = self._auth_repository.find_one(email, session)
        if user and self._password_hasher.verify(password, user.password):
            return user
        return None
