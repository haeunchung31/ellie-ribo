from dataclasses import dataclass
from datetime import datetime


class Acquisition:
    def get_complete_cnt(self):
        pass
    
    def get_pending_cnt(self):
        pass

    def get_failed_cnt(self):
        pass

    def get_source_type(self):
        pass

    def get_source_id(self):
        pass

    def get_date(self):
        pass

    def is_alarm(self):
        return self.get_failed_cnt() / self.get_complete_cnt() > 0.3        
