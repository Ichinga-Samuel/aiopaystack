from datetime import datetime
from typing import Literal

from .base import Base, Response, Currency

BearerType = Literal['subaccount', 'account', 'all-proportional', 'all']


class TransactionSplits(Base):
    """
    The Transaction Splits API enables merchants split the settlement for a transaction across their payout account,
    and one or more Subaccounts.
    """
    def __init__(self):
        super().__init__()
        url = '/split/{}'
        self.url = url.format

    async def create(self, *, name: str, type: Literal['percentage', 'flat'], currency: Currency,
                     subaccounts: list[dict], bearer_type: BearerType, bearer_subaccount: str) -> Response:
        """
        Create a split payment on your integration
        :param name: Name of the transaction split
        :param type: The type of transaction split you want to create. You can use one of the following: percentage | flat
        :param currency: Any of NGN, GHS, ZAR, or USD
        :param subaccounts: A list of object containing subaccount code and number of shares:
            eg. [{subaccount: ‘ACT_xxxxxxxxxx’, share: xxx},{...}]
        :param bearer_type: Any of subaccount | account | all-proportional | all
        :param bearer_subaccount: Subaccount code
        :return: Response Dict
        """
        data = {'name': name, 'type': type, 'currency': currency, 'subaccounts': subaccounts,
                'bearer_type': bearer_type, 'bearer_subaccount': bearer_subaccount}
        return await self.post(url=self.url(""), json=data)

    async def list(self, name: str, active: bool, from_: datetime | None | str = None, **kwargs):
        """
        List/search for the transaction splits available on your integration.
        :param name: The name of the split
        :param active: Any of true or false
        :param from_: A timestamp from which to start listing splits, the optional "from" argument is to be added this way with a trailing underscore
        :param kwargs: Optional keyword query parameters as keyword args
        :return: Response
        """
        params = {key: value for key, value in (('name', name), ('active', active), ('from', from_), *kwargs.items()) if value}
        return await self.get(url=self.url(''), params=params)

    async def search(self, name: str, active: bool, from_: datetime | None | str = None, **kwargs):
        """
        Does the exact same thing as list
        :param name: The name of the split
        :param active: Any of true or false
        :param from_: A timestamp from which to start listing splits, the optional from argument is to be added this way with a trailing underscore
        :param kwargs: Optional keyword query parameters as keyword args
        :return: Response
        """
        params = {key: value for key, value in (('name', name), ('active', active), ('from', from_), *kwargs.items()) if value}
        return await self.get(url=self.url(''), params=params)

    async def fetch(self, *, id: str):
        """
        Get details of a split on your integration
        :param id: The id of the split
        :return: Response
        """
        params = {'id': id}
        return await self.get(url=self.url(f"{id}"), params=params)

    async def update(self, *, id: str, name: str, active: bool, **kwargs):
        """
        Update a transaction split details on your integration
        :param id: Split ID
        :param name: The name of the split
        :param active: Any of true or false
        :param kwargs: Optional Parameters
        :return: Response
        """
        data = {'name': name, active: active, **kwargs}
        return await self.put(url=self.url(f"{id}"), json=data)

    async def add_split_subaccount(self, *, id: str, subaccount: str, share: int):
        """
        Add a Subaccount to a Transaction Split, or update the share of an existing Subaccount in a Transaction Split
        :param id: Split Id
        :param subaccount: This is the sub account code
        :param share: This is the transaction share for the subaccount
        :return:
        """
        data = {'id': id, 'subaccount': subaccount, 'share': share}
        return await self.post(url=self.url(f"{id}/subaccount/add"), json=data)

    async def remove_subaccount_from_split(self, *, id: str, subaccount: str):
        """
        Remove a subaccount from a transaction split
        :param id: Split Id
        :param subaccount: This is the sub account code
        :return:
        """
        data = {'id': id, 'subaccount': subaccount}
        return await self.post(url=self.url(f"{id}/subaccount/remove"), json=data)
