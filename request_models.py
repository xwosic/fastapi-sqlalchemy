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


class PetParams(BaseModel):
    id: Optional[int]
    age: Optional[int]
    name: Optional[str]
    pet_type: Optional[str]


class GetPetParams(PetParams):
    pass