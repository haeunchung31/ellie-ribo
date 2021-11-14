from dataclasses import dataclass
from enum import Enum, auto

class SaleType(Enum):
    WD = auto()
    CWD	= auto()
    VWD	= auto()
    New	= auto()
    COD	= auto()
    Con	= auto()
    ConLw = auto()
    ConLI = auto()	
    ConLD = auto()
    Oth	= auto()

class SaleCondition(Enum):
    Normal = auto()
    Abnormal = auto()
    AdjLand = auto()
    Alloca = auto()
    Family = auto()
    Partial = auto()


@dataclass
class Sale:
    house_id: str
    sale_type: SaleType
    sale_condition: SaleCondition
    mo_sold: int
    yr_sold: int
    sale_price: int
