from datetime import datetime
from typing import Literal

from .base import Base


class TransferRecipient(Base):
    """
    The Transfer Recipients API allows you create and manage beneficiaries that you send money to
    """
    def __init__(self):
        super().__init__()
        url = "/transferrecipient/"
        self.url = url.format

    async def create(self, type: Literal['nuban', 'mobile_money', 'basa'], name: str, account_number: str = "", bank_code: str = "", **kwargs):
        """
        Creates a new recipient. A duplicate account number will lead to the retrieval of the existing record.
        :param type: Recipient Type. It could be one of: nuban, mobile_money or basa
        :param name: A name for the recipient
        :param account_number: Required if type is nuban or basa
        :param bank_code: Required if type is nuban or basa. You can get the list of Bank Codes by calling the List Banks endpoint.
        :param kwargs:
        :return: Response
        """
        data = {key: value for key, value in (('type', type), ('name', name), ('account_number', account_number), ('bank_code', bank_code),
                                              *kwargs.items()) if value}
        return await self.post(url=self.url(""), json=data)

    async def bulk_create(self, *, batch: list[dict]):
        """
        Create multiple transfer recipients in batches. A duplicate account number will lead to the retrieval of the existing record.
        :param batch: A list of transfer recipient object. Each object should contain type, name, and bank_code.
         Any Create Transfer Recipient param can also be passed.
        :return: Response
        """
        data = {'batch': batch}
        return await self.post(url=self.url("bulk"), json=data)

    async def list(self, *, perPage: int = 50, page: int = 1, from_: datetime | None = None, to: datetime | None = None):
        """
        List transfer recipients available on your integration
        :param page:    Specify exactly what page you want to retrieve. If not specify we use a default value of 1.
        :param perPage: Specify how many records you want to retrieve per page. If not specify we use a default value of 50.
        :param from_:   A timestamp from which to start listing transfer recipients e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
        :param to:      A timestamp at which to stop listing transfer recipients e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
        :return: Response
        """
        params = {key: value for key, value in (('from', from_), ('to', to), ('perPage', perPage), ('page', page)) if value}
        return await self.get(url=self.url(""), params=params)

    async def fetch(self, *, id_or_code):
        """
        Fetch the details of a transfer recipient
        :param id_or_code: An ID or code for the recipient whose details you want to receive
        :return: Response
        """
        params = {'id_or_code': id_or_code}
        return await self.get(url=self.url(f"{id_or_code}"), params=params)

    async def update(self, *, id_or_code: str, name: str, email: str = ""):
        """
        Update an existing recipient. Any duplicate account number will lead to the retrieval of the existing record.
        :param id_or_code:
        :param name: A name for the recipient
        :param email: Email address of the recipient
        :return: Response
        """
        data = {'name': name, 'id_or_code': id_or_code}
        data.update({"email": email}) if email else ...
        return await self.put(url=self.url(f"{id_or_code}"), json=data)

    async def delete_transfer_recipient(self, *, id_or_code: str):
        """
        Deletes a transfer recipient (sets the transfer recipient to inactive)
        :param id_or_code: Transfer Recipient
        :return: Response
        """
        data = {'id_or_code': id_or_code}
        return await self.delete(url=self.url(f"{id_or_code}"), json=data)
