from pydantic import BaseModel
from api.dto.uses_cases.role_uses_cases import ValidRoleName

class Role(BaseModel):
    name: ValidRoleName