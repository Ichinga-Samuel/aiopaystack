from datetime import datetime

from .base import Base


class BulkCharge(Base):
    """
    The Bulk Charges API allows you create and manage multiple recurring payments from your customers
    """
    def __init__(self):
        super().__init__()
        url = "/bulkcharge/"
        self.url = url.format

    async def initiate(self, charges: list[dict]):
        """
        Send an array of objects with authorization codes and amount (in kobo if currency is NGN, pesewas,
        if currency is GHS, and cents, if currency is ZAR ) so we can process transactions as a batch.
        :param charges: A list of charge object. Each object consists of an authorization, amount and reference
        :return: Response
        """
        return await self.post(url=self.url(""), json=charges)

    async def list(self, *, perPage: int = 50, page: int = 1, from_: datetime | None | str = None, to: datetime | None | str = None):
        """
        This lists all bulk charge batches created by the integration. Statuses can be active, paused, or complete.
        :param perPage: Specify how many records you want to retrieve per page. If not specify we use a default value of 50.
        :param page: Specify exactly what page you want to retrieve. If not specify we use a default value of 1.
        :param from_: A timestamp from which to start listing batches e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
        :param to: A timestamp at which to stop listing batches e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
        :return: Response
        """
        params = {'perPage': perPage, 'page': page} | {key: value for key, value in (('from', from_), ('to', to)) if value}
        return await self.get(url=self.url(""), params=params)

    async def fetch_bulk_charge_batch(self, *, id_or_code: str):
        """
        This endpoint retrieves a specific batch code. It also returns useful information on its progress by way of the total_charges
         and pending_charges attributes.
        :param id_or_code: An ID or code for the charge whose batches you want to retrieve.
        :return: Response
        """
        return await self.get(url=self.url(f"{id_or_code}"))

    async def fetch_charges_in_a_batch(self, *, id_or_code: str, perPage: int = 50, page: int = 1, from_: datetime | None | str = None,
                                       to: datetime | None | str = None):
        """
        This endpoint retrieves the charges associated with a specified batch code. Pagination parameters are available.
        You can also filter by status. Charge statuses can be pending, success or failed.
        :param id_or_code: An ID or code for the batch whose charges you want to retrieve.
        :param perPage: Specify how many records you want to retrieve per page. If not specify we use a default value of 50.
        :param page: Specify exactly what page you want to retrieve. If not specify we use a default value of 1.
        :param from_: A timestamp from which to start listing charges e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
        :param to: A timestamp at which to stop listing charges e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
        :return: Response
        """
        params = {'perPage': perPage, 'page': page} | {key: value for key, value in (('from', from_), ('to', to)) if value}
        return await self.get(url=self.url(f"{id_or_code}/charges"), params=params)

    async def pause_bulk_charge(self, *, batch_code: str):
        """
        Use this endpoint to pause processing a batch
        :param batch_code: The batch code for the bulk charge you want to pause
        :return: Response
        """
        return await self.get(url=self.url(f"pause/{batch_code}"))

    async def resume_bulk_charge(self, *, batch_code: str):
        """
        Use this endpoint to resume processing a batch
        :param batch_code: The batch code for the bulk charge you want to resume
        :return: Response
        """
        return await self.get(url=self.url(f"resume/{batch_code}"))
