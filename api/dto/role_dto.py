from pydantic import BaseModel
from api.dto.uses_cases.role_uses_cases import ValidRoleName

class RoleDto(BaseModel):
    name: ValidRoleName
    
class RoleResponse(BaseModel):
    id: int
    name: ValidRoleName
    
class RoleData(BaseModel):
    role_list: list[RoleResponse]
    