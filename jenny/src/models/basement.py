from space import Space

from dataclasses import dataclass
from enum import Enum, auto

class BasementType(Enum):
    type1 = auto()
    type2 = auto()
    unfinished = auto()

@dataclass
class Basement(Space):
    fin_sf1: int
    fin_sf2: int
    unf_sf: int
    total_sf: int

    def get_space_size(self, type):
        if type == BasementType.type1:
            return self.fin_sf1
        elif type == BasementType.type2:
            return self.fin_sf2
        else:
            return self.unf_sf
    
    def get_total_size(self):
        return self.total_sf