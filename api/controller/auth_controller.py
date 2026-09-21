from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from api.services.auth_services import AuthServices

auth_service = AuthServices()

class AuthController:
    def login(self, email: str, password: str, session) -> dict:
        try:
            user, token = auth_service.login(email, password, session)
            if user is None:
                raise HTTPException(status_code=401, detail="Invalid email or password")
        except IntegrityError:
            session.rollback()
            raise HTTPException(status_code=500, detail="An error occurred during login")
        return {"message": "Login successful", "user": user.model_dump(), "access_token": token, "token_type": "bearer"}