from house import House
from typing import *

from house_stat import HouseStat


def run(houses: List[House]) -> None:
    for house in houses:
        # TODO(mark): 새로운 meta 가 발견되면 house_meta_schema 에  넣어주기.
        for key in house.meta.keys():
            pass
            # HouseMetaSchema(house.origin, key, '')

    date = '2022-01-01' # TODO(mark)
    avg = 1.1 # TODO(mark)
    median = 1.0 # TODO(mark)
    house_stat = HouseStat(date=date, avg=avg, median=median)
    # Save house stat
    return

