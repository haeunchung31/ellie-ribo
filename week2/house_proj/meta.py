from dataclasses import dataclass
from typing import *

from house import House

@dataclass
class Meta:
    type: str
    field: str

"""
class Meta:
    def __init__(self, type: str, field: str) -> None:
        self.type = type
        self.field = field
"""

"""
metas: List[Meta] = [
    Meta('area', 'first_flr_sf'),
    Meta('area', 'second_flr_sf'),
    Meta('area', 'lot_area'),
    Meta('price', 'sale_price')
]
"""
metas: List[Meta] = []
for field in House.get_all_meta_fields():
    metas.append(Meta('Unknown', field))
