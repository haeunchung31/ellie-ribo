from dataclasses import dataclass
from typing import *


@dataclass
class House:
    id: int
    m_s_sub_class: int
    lot_area: int
    first_flr_sf: int
    second_flr_sf: int
    sale_price: int


    @staticmethod
    def get_all_meta_fields() -> List[str]:
        results: List[str] = []
        for key in House.__dataclass_fields__.keys():
            if key in ['id', 'm_s_sub_class']:
                pass
            else:
                results.append(key)
        return results
