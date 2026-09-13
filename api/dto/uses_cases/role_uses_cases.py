from pydantic import AfterValidator
from typing import Annotated

def valid_role_name(name: str) -> str:
    if(name not in ["admin", "user"]):
        raise ValueError("The role name must be either 'admin' or 'user'")
    return name

ValidRoleName = Annotated[str, AfterValidator(valid_role_name)]