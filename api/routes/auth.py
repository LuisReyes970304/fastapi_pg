from fastapi import APIRouter, Depends
from api.controller.auth_controller import AuthController
from api.utils.session_util import get_session
from sqlmodel import Session
from api.dto.auth_dto import LoginModel

router = APIRouter(prefix="/users", tags=["Auth"])
auth_controller = AuthController()

@router.post("/login/{email}")
async def login(login_model: LoginModel, session: Session = Depends(get_session)):
    user = auth_controller.login(login_model.email, login_model.password, session)
    return user