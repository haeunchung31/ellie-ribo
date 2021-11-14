from space import Space

class Bathroom(Space):

    def __init__(self, **kwargs) -> None:
        self.above = True if kwargs.get('location') == 'above' else False
        self.full = True if kwargs.get('is_full') else False
        self.full_count = kwargs.get('full_count')
        self.half_count = kwargs.get('full_count')
        self.full_count_bsmt = kwargs.get('full_count_bsmt')
        self.half_count_bsmt = kwargs.get('full_count_bsmt')

    def get_space_count(self):        
        if self.full:
            return self.full_count if self.above else self.full_count_bsmt
        else:
            return self.half_count if self.above else self.half_count_bsmt

    