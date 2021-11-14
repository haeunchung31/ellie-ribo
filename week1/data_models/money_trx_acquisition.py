# Internal dependencies
from data_models.core.acquisition import Acquisition
from data_models.core.cron_job import CronJob

# External dependencies
from datetime import datetime
from dataclasses import dataclass


@dataclass
class MoneyTrxAcquisition(CronJob, Acquisition):
    """
    Daily 로 User 와 MoneyTrx 를 join 해서 아래 필드들을 채워줌
    """
    sent_cnt: int
    recieve_cnt: int
    type: str
    trx_id: int
    date: datetime

    def get_source_type(self):
        return 'money_trx'

    def get_source_id(self):
        return self.trx_id

    def get_date(self):
        return self.date

    def get_unopened(self):
        return self.sent_cnt - self.recieve_cnt

    @staticmethod
    def do_cron_job():
        # MoneyTrx 와 User 를 조인해서 MoneyTrxAcquisition 을 만들어서 저장
        pass

