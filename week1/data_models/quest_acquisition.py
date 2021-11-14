# Internal dependencies
from data_models.core.acquisition import Acquisition
from data_models.core.cron_job import CronJob

# External dependencies
from datetime import datetime
from dataclasses import dataclass


@dataclass
class QuestAcquisition(CronJob, Acquisition):
    """
    Daily 로 User 와 UserQuest 를 join 해서 아래 필드들을 채워줌
    """
    fail_cnt: int
    complete_cnt: int
    quest_id: int
    date: datetime

    def get_source_type(self):
        return 'quest'

    def get_source_id(self):
        return self.quest_id

    def get_date(self):
        return self.date


    @staticmethod
    def do_cron_job():
        # Quest 와 UserQuest 를 조인해서 QuestAcquisition 을 만들어서 저장
        pass

