from typing import Optional
from pydantic import BaseModel


class UserParams(BaseModel):
    id: Optional[int]
    name: Optional[str] = None
    fullname: Optional[str] = None
    nickname: Optional[str] = None


class GetUserParams(UserParams):
    pass


class UpdateUserParams(UserParams):
    pass


class InsertUserParams(UserParams):
    pass
