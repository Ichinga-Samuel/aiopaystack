from datetime import datetime
from typing import Literal

from .base import Base


class Transfers(Base):
    """
    The Transfers API allows you automate sending money to your customers
    """

    def __init__(self):
        super().__init__()
        url = "/transfer/"
        self.url = url.format

    async def initiate(self, source: str, amount: int, recipient: str, **kwargs):
        """
        Status of transfer object returned will be pending if OTP is disabled. In the event that an OTP is required, status will read otp.
        :param source: Where should we transfer from? Only balance for now
        :param amount: Amount to transfer in kobo if currency is NGN and pesewas if currency is GHS.
        :param recipient: Code for transfer recipient
        :param kwargs: Optional Parameters
        :return: Response
        """
        data = {'source': source, 'amount': amount, "recipient": recipient, **kwargs}
        return await self.post(url=self.url(""), json=data)

    async def finalize(self, *, transfer_code: str, otp: str,):
        """
        Finalize an initiated transfer
        :param transfer_code: The transfer code you want to finalize
        :param otp: OTP sent to business phone to verify transfer
        :return: Response
        """
        data = {'otp': otp, 'transfer_code': transfer_code}
        return await self.post(url=self.url("finalize_transfer"), json=data)

    async def initiate_bulk_transfer(self, *, source: str, transfers: list[dict['amount', 'recipient', 'reference']], **kwargs):
        """
        You need to disable the Transfers OTP requirement to use this endpoint.
        :param source: Where should we transfer from? Only balance for now
        :param transfers: A list of transfer object. Each object should contain
        :return: Response
        """
        data = {'source': source, 'transfers': transfers, **kwargs}
        return await self.post(url=self.url("bulk"), json=data)

    async def list(self, *, customer: str, perPage: int = 50, page: int = 1, from_: datetime | None | str = None, to: datetime | None | str = None,
                   **kwargs):
        """
        List the transfers made on your integration.
        :param customer: Filter by customer ID
        :param perPage: Specify how many records you want to retrieve per page. If not specify we use a default value of 50.
        :param page: Specify exactly what transfer you want to page. If not specify we use a default value of 1.
        :param from_: A timestamp from which to start listing transfer e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
        :param to: A timestamp at which to stop listing transfer e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
        :return: Response
        """
        params = {key: value for key, value in (('customer', customer), ('perPage', perPage), ('page', page), ('from', from_), ('to', to),
                                                *kwargs.items())}
        return await self.get(url=self.url(""), params=params)

    async def fetch(self, *, id_or_code: str):
        """
        Get details of a transfer on your integration.
        :param id_or_code: The transfer ID or code you want to fetch
        :return: Response
        """
        return await self.get(url=self.url(f"{id_or_code}"))

    async def verify(self, *, reference: str):
        """
        Verify the status of a transfer on your integration.
        :param reference: Verify the status of a transfer on your integration.
        :return: Response
        """
        return await self.get(url=self.url(f"verify/{reference}"))
