from pydantic import BaseModel, EmailStr
from api.dto.uses_cases.user_uses_cases import Name, Password

class UserData(BaseModel):
    users: list[dict]

class UserDto(BaseModel):
    name: Name
    email: EmailStr
    password: Password
    role: str
    
