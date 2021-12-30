from typing import Optional
from pydantic import BaseModel


class GetUsersParams(BaseModel):
    id: Optional[int]
    name: Optional[str] = None
    fullname: Optional[str] = None
    nickname: Optional[str] = None
  