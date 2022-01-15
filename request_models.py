from typing import Optional
from pydantic import BaseModel


class UsersParams(BaseModel):
    id: Optional[int]
    name: Optional[str] = None
    fullname: Optional[str] = None
    nickname: Optional[str] = None


class GetUsersParams(UsersParams):
    pass


class UpdateUserParams(UsersParams):
    pass
