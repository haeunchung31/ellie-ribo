from typing import Any
from dataclasses import dataclass


@dataclass
class House:
    price: float
    meta: Any
    origin: str
    

@dataclass
class HouseMetaSchema:
    origin: str
    key: str
    description: str

