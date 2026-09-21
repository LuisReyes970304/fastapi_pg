from fastapi import APIRouter, Depends
from api.controller.auth_controller import AuthController
from api.utils.session_util import get_session
from sqlmodel import Session

router = APIRouter(prefix="/users", tags=["Auth"])
auth_controller = AuthController()

@router.post("/login/{email}")
async def login(email: str, password: str, session: Session = Depends(get_session)):
    return auth_controller.login(email, password, session)