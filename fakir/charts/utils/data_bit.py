from pydantic import BaseModel
from enum import Enum
from typing import List, Dict

class Value(BaseModel):
    column_name: str
    min: float = 0
    max: float = 100
    digits: int = 2


class Label(BaseModel):
    column_name: str
    values_list: List[str]

