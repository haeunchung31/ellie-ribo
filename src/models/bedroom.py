from space import Space

from dataclasses import dataclass

@dataclass
class Bedroom(Space):
    count:int

    def get_space_count(self):
        return self.count
    