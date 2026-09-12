from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    email: str
    password: str
    role_id: int
    is_active: bool = Field(default=True)
    

