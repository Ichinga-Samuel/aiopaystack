from datetime import datetime

from .base import Base


class Settlements(Base):
    """
    The Settlements API allows you gain insights into payouts made by Paystack to your bank account
    """

    def __init__(self):
        super().__init__()
        url = "/settlement/{}"
        self.url = url.format

    async def fetch(self, *, perPage: int = 50, page: int = 1, subaccount: str = 'none', from_: datetime | None | str = None,
                    to: datetime | None | str = None):
        """
        :param page: Specify exactly what page you want to retrieve. If not specify we use a default value of 1.
        :param perPage: Specify how many records you want to retrieve per page. If not specify we use a default value of 50.
        :param subaccount: Provide a subaccount ID to export only settlements for that subaccount. Set to none to export only transactions for the
                           account.
        :param from_: A timestamp from which to start listing settlements e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
        :param to: A timestamp at which to stop listing settlements e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
        :return:
        """
        params = {key: value for key, value in (('perPage', perPage), ('page', page), ('subaccount', subaccount), ('from', from_),
                                                ('to', to)) if value}
        return await self.get(url=self.url(""), params=params)

    async def fetch_settlement_transactions(self, *, perPage: int = 50, page: int = 1, from_: datetime | None | str = None, to: datetime | None | str = None):
        """
        :param page: Specify exactly what page you want to retrieve. If not specify we use a default value of 1.
        :param perPage: Specify how many records you want to retrieve per page. If not specify we use a default value of 50.
        :param from_: A timestamp from which to start listing settlement transactions e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
        :param to: A timestamp at which to stop listing settlement transactions e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
        :return:
        """
        params = {key: value for key, value in (('perPage', perPage), ('page', page), ('from', from_), ('to', to)) if value}
        return await self.get(url=self.url(""), params=params)
