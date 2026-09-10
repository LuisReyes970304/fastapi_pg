from sqlmodel import SQLModel, Field

class Role(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str = Field(unique=True, index=True)