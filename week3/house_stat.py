from dataclasses import dataclass


@dataclass
class HouseStat:
    date: str
    avg: float
    median: float
