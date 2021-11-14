from dataclasses import dataclass

@dataclass
class HouseStat:
    date: str
    type: str
    field: str
    m_s_sub_class: str
    value: float
