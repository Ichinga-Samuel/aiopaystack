from datetime import datetime

from .base import Base


class Invoice(Base):
    """
    The Invoices API allows you issue out and manage payment requests
    """
    def __init__(self):
        super().__init__()
        url = "/paymentrequest/"
        self.url = url.format

    async def create(self, *, customer: str, amount: int, **kwargs):
        """
        Create an invoice for payment on your integration
        :param customer: Customer id or code
        :param amount: Payment request amount. It should be used when line items and tax values aren't specified.
        :param kwargs:
        :return: Response
        """
        data = {"customer": customer, "amount": amount, **kwargs}
        return await self.post(url=self.url(""), json=data)

    async def list(self, customer: str, status: str, currency: str, include_archive: str, from_: datetime | None = None, perPage: int = 50, page: int = 1, **kwargs):
        """
        List the invoice available on your integration.
        :param page: Specify exactly what page you want to retrieve. If not specify we use a default value of 1.
        :param perPage: Specify how many records you want to retrieve per page. If not specify we use a default value of 50.
        :param customer: Filter by customer ID
        :param status: Filter by invoice status
        :param currency: Filter by currency. Allowed values are NGN, GHS, ZAR and USD
        :param include_archive: Show archived invoices
        :param from_: from A timestamp from which to start listing invoice e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
        :param kwargs:
        :return: Response
        """
        params = {"customer": customer, "status": status, "currency": currency, "include_archive": include_archive, "perPage": perPage,
                  "page": page}
        params.update({'from': from_, **kwargs})
        return await self.get(url=self.url(""), params=params)

    async def view(self, *, id_or_code: str):
        """
        Get details of an invoice on your integration.
        :param id_or_code: The invoice ID or code you want to fetch
        :return: Response
        """
        params = {'id_or_code': id_or_code}
        return await self.get(url=self.url(f"{id_or_code}"), params=params)

    async def verify(self, *, code: str):
        """
        Verify details of an invoice on your integration.
        :param code: Invoice code
        :return: Response
        """
        params = {'code': code}
        return await self.get(url=self.url(f"verify/{code}"), params=params)

    async def send_notification(self, *, code: str):
        """
        :param code: Invoice code
        :return: Response
        """
        params = {'code': code}
        return await self.post(url=self.url(f"notify/{code}"), params=params)

    async def invoice_totals(self):
        """
        Get invoice metrics for dashboard
        :return: Response
        """
        return await self.get(url=self.url("totals"))

    async def finalize_invoice(self, *, code: str):
        """
        Finalize a Draft Invoice
        :param code: Invoice code
        :return: Response
        """
        data = {'code': code}
        return await self.post(url=self.url(f"finalize/{code}"), json=data)

    async def update(self, *, id_or_code: str, customer: str, amount: int, **kwargs):
        """
        Update an invoice details on your integration
        :param id_or_code: Invoice ID or slug
        :param customer: Customer id or code
        :param amount: Payment request amount. Only useful if line items and tax values are ignored. endpoint will throw a friendly warning
         if neither is available.
        :param kwargs:
        :return: Response
        """
        data = {'id_or_code': id_or_code, 'customer': customer, 'amount': amount, **kwargs}
        return await self.put(url=self.url(f"{id_or_code}"), json=data)

    async def archive(self, *, id_or_code: str):
        """
        Used to archive an invoice. Invoice will no longer be fetched on list or returned on verify.
        :param id_or_code: Code of the invoice
        :return: Response
        """
        return await self.post(url=self.url(f"archive/{id_or_code}"))
