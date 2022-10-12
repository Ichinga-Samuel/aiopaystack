from datetime import datetime

from .base import Base


class SubAccounts(Base):
    """
    The Subaccounts API allows you create and manage subaccounts on your integration.
    Subaccounts can be used to split payment between two accounts (your main account and a sub account)
    """
    def __init__(self):
        super().__init__()
        url = "/subaccount/"
        self.url = url.format

    async def create(self, *, business_name: str, settlement_bank: str, account_number: str, percentage_charge: float, description: str, **kwargs):
        """
        Create a subacount on your integration
        :param description: A description for this subaccount
        :param percentage_charge: A description for this subaccount
        :param account_number: Bank Account Number
        :param settlement_bank: Bank Code for the bank. You can get the list of Bank Codes by calling the List Banks endpoint.
        :param business_name: Name of business for subaccount
        :param kwargs:
        :return:
        """
        data = {'business_name': business_name, 'settlement_bank': settlement_bank, 'account_number': account_number,
                "percentage_charge": percentage_charge, 'description': description} | kwargs
        return await self.post(url=self.url(""), json=data)

    async def list(self, *, perPage: int = 50, page: int = 1, from_: datetime | None = None, to: datetime | None = None):
        """
        List subaccounts available on your integration.
        :param perPage: Specify how many records you want to retrieve per page. If not specify we use a default value of 50.
        :param page: Specify exactly what page you want to retrieve. If not specify we use a default value of 1.
        :param to:
        :param from_:
        :return:
        """
        params = {'perPage': perPage, 'page': page} | {key: value for key, value in (('from', from_), ('to', to)) if value}
        return await self.get(url=self.url(""), params=params)

    async def fetch(self, *, id_or_code: str):
        """
        Get details of a subaccount on your integration
        :param id_or_code: The subaccount ID or code you want to fetch
        :return:
        """
        return await self.get(url=self.url(f"{id_or_code}"))

    async def update(self, *, id_or_code: str, business_name: str, settlement_bank: str, **kwargs):
        """
        Update a subaccount details on your integration
        :param settlement_bank:
        :param business_name:
        :param id_or_code:
        :param kwargs:
        :return:
        """
        data = {'id_or_code': id_or_code, 'business_name': business_name, 'settlement_bank': settlement_bank} | kwargs
        return await self.put(url=self.url(""), json=data)
