from dataclasses import dataclass

@dataclass
class House:
    id: str
    year_built: int
    year_remod_add: int
    bldg_type:str
    first_flr_sq: float
    second_flr_sq: float
    gr_liv_area: float
    tot_rms_abv_grd: int