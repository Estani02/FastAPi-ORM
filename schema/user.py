from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
  # id: Optional[str] = None
  field_1:str
  author:str
  description:str
  my_numeric_field:int
  