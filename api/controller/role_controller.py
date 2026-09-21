from fastapi import HTTPException
from api.dto.role_dto import RoleData, RoleResponse
from api.services.role_service import RoleServices

class RoleController:
    def __init__(self):
        self.role_services = RoleServices()

    def list_roles(self, session) -> RoleData:
        role_list = self.role_services.find_all(session)
        return RoleData(role_list=[role.model_dump() for role in role_list])

    def find_by_id(self, id: int, session) -> RoleResponse:
        role = self.role_services.find_one(id, session)
        if role is None:
            raise HTTPException(status_code=404, detail="Role not found")
        return RoleResponse(**role.model_dump())