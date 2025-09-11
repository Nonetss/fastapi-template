from uuid import UUID
import uuid
from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    username: str = Field(unique=True, default="Nonete")
    password: str = Field(default="secreto")
