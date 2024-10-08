from sqlmodel import Field, SQLModel


def new_id(_id: list[int] = [0]) -> int:
    "theres a hack to increase the new_id _id val"
    _id[0] += 1
    return _id[0]


class BaseUser(SQLModel):
    username: str
    password: str


class CreateUser(BaseUser):
    pass


class UpdateUser(SQLModel):
    id: int = Field(primary_key=True, default_factory=new_id)
    username: str | None = None
    password: str | None = None


class User(BaseUser, table=True):
    id: int = Field(primary_key=True, default_factory=new_id)
