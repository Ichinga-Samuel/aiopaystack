from typing import Literal

from .base import Base


class Plan(Base):
    """
    The Plans API allows you create and manage installment payment options on your integration
    """
    def __init__(self):
        super().__init__()
        url = "/plan/"
        self.url = url.format

    async def create(self, *, name: str, amount: int, interval: Literal['daily', 'weekly', 'monthly', 'biannually', 'annually'], **kwargs):
        """
        Create a plan on your integration
        :param name: Name of plan
        :param amount: Amount should be in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR
        :param interval: Interval in words. Valid intervals are: daily, weekly, monthly,biannually, annually.
        :param kwargs: Optional keyword args to form the body of the request
        :return: Json data from paystack API.
        """
        data = {'name': name, 'amount': amount, 'interval': interval} | kwargs
        return await self.post(url=self.url(""), json=data)

    async def list(self, perPage: int, page: int, **kwargs):
        """
        List plans available on your integration.
        :param perPage: Specify how many records you want to retrieve per page.
        :param page: Specify exactly what page you want to retrieve.
        :param kwargs: Keyword args to form the query params
        :return: Response
        """
        params = {"perPage": perPage, "page": page, **kwargs}
        return await self.get(url=self.url(""), params=params)

    async def fetch(self, *, id_or_code: str):
        """
        Get details of a plan on your integration.
        :param id_or_code: The plan ID or code you want to fetch
        :return: Response
        """
        params = {'id_or_code': id_or_code}
        return await self.get(url=self.url(f"{id_or_code}"), params=params)

    async def update(self, *, id_or_code: str, name: str, amount: str, interval: Literal['daily', 'weekly', 'monthly', 'biannually', 'annually'],
                     **kwargs):
        """
        Update a plan details on your integration
        :param id_or_code: Plan's ID or code
        :param name: Name of plan
        :param amount: Amount should be in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR
        :param interval: Interval in words. Valid intervals are: daily, weekly, monthly,biannually, annually.
        :param kwargs: Optional keyword args to form the body of the request
        :return: Response
        """
        data = {'id_or_code': id_or_code, 'name': name, 'amount': amount, 'interval': interval, **kwargs}
        return await self.put(url=self.url(f"{id_or_code}"), json=data)
