from enum import Enum
from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel


#Enums for constrains
class Gender(str, Enum):
    male="Male",
    female="Female"


class Role(str, Enum):
    user="USER",
    admin="ADMIN"



class User(BaseModel):
    id:Optional[UUID]=uuid4()
    name:str
    gender:Gender
    role:list[Role]