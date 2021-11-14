from data_models.money_trx_acquisition import MoneyTrxAcquisition as CoreMoneyTrxAcquisition


class MoneyTrxAcquisition(CoreMoneyTrxAcquisition):

    def get_type(self):
        raise Exception('카트는 타입 없어요. 잘못된 분석을 하고 계십니다.')

    def get_unopened(self):
        return super().get_unopened() * 2

    def is_alarm(self):
        return True

