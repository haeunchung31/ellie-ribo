from datetime import datetime
from dataclasses import dataclass


"""
Models
"""
@dataclass
class User:
    id: str


@dataclass
class Quest:
    id: str


@dataclass
class UserQuest:
    id: str
    user_id: str
    quest_id: str
    progress: str


@dataclass
class MonyTrx:
    id: str
    user_id: str
    type: str
    amount: int
