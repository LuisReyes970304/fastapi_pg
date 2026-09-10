from pydantic import AfterValidator
from typing import Annotated

def valid_name(name: str) -> str:
    if len(name) <= 2:
        raise ValueError("The name cannot be shorter than 2 characters")
    if len(name) > 50:
        raise ValueError("The name cannot be longer than 50 characters")
    if not name.replace(" ", "").isalpha():
        raise ValueError("The name can only contain letters and spaces")
    return name

def valid_password(password: str) -> str:
    if len(password) < 8:
        raise ValueError("The password cannot be shorter than 8 characters")
    if len(password) > 50:
        raise ValueError("The password cannot be longer than 50 characters")
    if not any(char.isdigit() for char in password):
        raise ValueError("The password must contain at least one digit")
    if not any(char.isupper() for char in password):
        raise ValueError("The password must contain at least one uppercase letter")
    if not any(char.islower() for char in password):
        raise ValueError("The password must contain at least one lowercase letter")
    return password

Name = Annotated[str, AfterValidator(valid_name)]

Password = Annotated[str, AfterValidator(valid_password)]

