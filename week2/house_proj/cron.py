from typing import *
import csv
import numpy as np

from house import House
from house_stat import HouseStat
from meta import Meta, metas


HOUSES: List[House] = []


with open('train.csv') as csvfile:
    reader = csv.reader(csvfile)
    next(reader, None)

    for row in reader:
        HOUSES.append(House(int(row[0]), int(row[1]), int(row[4]), int(row[43]), int(row[44]), int(row[80])))


M_S_SUB_CLASS_HOUSE_DICT: Dict[int, List[House]] = dict()

# Common Grouping.
""" TODO(Daisy) 
DictUtil.group(HOUSES, 'm_s_sub_class')
"""
for house in HOUSES:
    if house.m_s_sub_class in M_S_SUB_CLASS_HOUSE_DICT:
        M_S_SUB_CLASS_HOUSE_DICT[house.m_s_sub_class].append(house)
    else:
        M_S_SUB_CLASS_HOUSE_DICT[house.m_s_sub_class] = [house]

"""
1: {
    House0,
    House1,
    ...
}
"""
HOUSE_STATS: List[HouseStat] = []

for meta in metas:
    for key in M_S_SUB_CLASS_HOUSE_DICT.keys():
        houses: List[House] = M_S_SUB_CLASS_HOUSE_DICT[key]

        values: List[int] = []
        for house in houses:
            values.append(getattr(house, meta.field))
        # values: List[int] = list(map(lambda x: getattr(x, meta.field), houses))

        HOUSE_STATS.append(HouseStat('2021-11-14', meta.type, meta.field, key, np.mean(values)))

# print(HOUSE_STATS)
