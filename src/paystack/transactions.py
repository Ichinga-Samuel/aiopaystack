from typing import Literal
from datetime import datetime

from .base import Base


class Transactions(Base):
    """
    The Transactions API allows you create and manage payments on your integration
    """
    def __init__(self):
        super().__init__()
        url = '/transaction/{}'
        self.url = url.format

    async def initialize(self, *, email: str, amount: str, **kwargs):
        """
        Initialize transaction. Email and amount are required fields
        :param amount: Amount should be in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR
        :param email: Customer's email address
        :param kwargs: optional params of request body as keyword arguments
        :return: json data from paystack API as a dict
        """
        data = kwargs | {'email': email, 'amount': amount}
        return await self.post(url=self.url('initialize'), json=data)

    async def verify(self, *, reference: str):
        """
        :param reference: The transaction reference used to initiate the transaction
        :return: json data from paystack API
        """
        return await self.get(url=self.url(f'verify/{reference}'))

    async def list(self, *, perPage: int = 50, page: int = 1, from_: datetime | None = None, **kwargs):
        """
        List transactions carried out on your integration.
        :param page:    Specify exactly what page you want to retrieve. If not specify we use a default value of 1.
        :param perPage: Specify how many records you want to retrieve per page. If not specify we use a default value of 50.
        :param from_: from should be added this way
        :param kwargs: Optional query parameters as keyword arguments
        :return: List of transactions as json data from paystack API
        """
        params = {"perPage": perPage, "page": page} | kwargs
        params.update(**{'from': from_}) if from_ else from_
        return await self.get(url=self.url(""), params=params)

    async def fetch(self, *, id):
        """
        Get details of a transaction carried out on your integration.
        :param id: id of a single transaction
        :return: json data from paystack API
        """

        return await self.get(url=self.url(f"/{id}"))

    async def charge_authorization(self, *, amount: str, email: str, authorization_code: str,  **kwargs):
        """
        :param authorization_code: Valid authorization code to charge
        :param email: Customer's email address
        :param amount:
        :param kwargs: optional params of request body as keyword arguments
        :return: json data from paystack API
        """
        data = kwargs | {'amount': amount, 'email': email, 'authorization_code': authorization_code}
        return await self.post(url=self.url("charge_authorization"), json=data)

    async def check_authorization(self, *, amount: str, email: str, authorization_code: str, **kwargs):
        """
        :param authorization_code: Valid authorization code to charge
        :param email:
        :param amount:
        :param kwargs: optional params of request body as keyword arguments
        :return: json data from paystack API
        """
        data = kwargs | {'amount': amount, 'email': email, 'authorization_code': authorization_code}
        return await self.post(url=self.url("check_authorization"), json=data)

    async def view_transaction_timeline(self, *, id_or_reference: str):
        """
        :param id_or_reference: id or reference of transaction
        :return: json data from paystack API
        """
        return await self.get(url=self.url(f"timeline/{id_or_reference}"))

    async def transaction_totals(self, *, perPage: int = 50, page: int = 1, from_: datetime | None = None, to: datetime | None = None):
        """
        If you specify a page number also specify a results per page. eg page=1, perPage=10
        You can specify from and to as query parameters
        :param page:
        :param perPage:
        :param to:
        :param from_: optional from query parameter
        :return: json data from paystack API
        """
        params = {key: value for key, value in [('from', from_), ('to', to)] if value}
        return await self.get(url=self.url(f"totals/{perPage}/{page}"), params=params)

    async def export_transactions(self, perPage: int = 50, page: int = 1, **kwargs):
        """
        If you specify a page number also specify a results per page. eg page=1, perPage=10
        :param perPage: Specify how many records you want to retrieve per page. If not specify we use a default value of 50.
        :param page: Specify exactly what page you want to retrieve. If not specify we use a default value of 1.
        :param kwargs:
        :return:
        """
        params = kwargs | {'perPage': perPage, 'page': page}
        return await self.get(url=self.url("export"), params=params)

    async def partial_debit(self, *, authorization_code: str, email: str, amount: str, currency: Literal['NGN', 'GHS', 'ZAR', 'USD'],  **kwargs):
        """
        Retrieve part of a payment from a customer
        authorization_code, currency, amount, email are required fields
        :param authorization_code: Valid authorization code to charge
        :param email: Customer's email address
        :param amount: Amount should be in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR
        :param currency: Specify the currency you want to debit. Allowed values are NGN, GHS, ZAR or USD.
        :param kwargs: keyword arguments form body of requests
        :return:
        """
        data = kwargs | {'authorization_code': authorization_code, 'email': email, "amount": amount, currency: currency}
        return await self.post(url=self.url("partial_debit"), json=data)
