from .base import Base
from typing import Literal


class Refund(Base):
    """
    The Refunds API allows you create and manage transaction refunds
    """
    def __init__(self):
        super().__init__()
        url = "/refund/{}"
        self.url = url.format


    async def create(self, *, transaction: str, **kwargs):
        """
        Initiate a refund on your integration
        :param transaction: Transaction reference or id
        :param kwargs:
        :return: Response
        """
        data = {'transaction': transaction, **kwargs}
        return await self.post(url=self.url(""), json=data)

    async def list(self, *, reference: str, currency: Literal['NGN', 'GHS', 'ZAR', 'USD'], **kwargs):
        """
        List refunds available on your integration.
        :param reference: Identifier for transaction to be refunded
        :param currency: Three-letter ISO currency. Allowed values are: NGN, GHS, ZAR or USD
        :param kwargs:
        :return: Response
        """
        params = {'reference': reference, 'currency':currency, **kwargs}
        return await self.get(url=self.url(""), params=params)

    async def fetch(self, *, reference: str):
        """
        Get details of a refund on your integration.
        :param reference: Identifier for transaction to be refunded
        :return: Response
        """
        params = {'reference': reference}
        return await self.get(url=self.url(f"{reference}"))
