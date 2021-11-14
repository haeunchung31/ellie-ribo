from space import Space

from dataclasses import dataclass

@dataclass
class Kitchen(Space):
    count:int
    quality: str

    def get_space_count(self):
        return self.count
    