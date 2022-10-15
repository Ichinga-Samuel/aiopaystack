from datetime import date

from .base import Base


class Disputes(Base):

    def __init__(self):
        super().__init__()
        url = "/dispute/{}"
        self.url = url.format

    async def list(self, *, from_: date, to: date, **kwargs):
        """
        List disputes filed against you
        :param from_: A timestamp from which to start listing dispute e.g. 2016-09-21
        :param to: A timestamp at which to stop listing dispute e.g. 2016-09-21
        :param kwargs:
        :return: Response
        """
        params = {'from': from_, 'to': to, **kwargs}
        return await self.get(url=self.url(""), params=params)

    async def fetch(self, *, id: str):
        """
        Get more details about a dispute.
        :param id: The dispute ID you want to fetch
        :return: Response
        """
        return await self.get(url=self.url(f"{id}"))

    async def list_transaction_disputes(self, *, id):
        """
        This endpoint retrieves disputes for a particular transaction
        :param id: The transaction ID you want to fetch
        :return: Response
        """
        return await self.get(url=self.url(f"transaction/{id}"))

    async def update(self, *, id: str, refund_amount: int, **kwargs):
        """
        Update details of a dispute on your integration
        :param id:
        :param refund_amount: the amount to refund, in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR
        :kwargs:
        :return:
        """
        return await self.put(url=self.url(f"{id}"), json={'refund_amount': refund_amount, **kwargs})

    async def add_evidence(self, *, id: str, customer_email: str, customer_name: str, customer_phone: str, service_details: str, **kwargs):
        """
        Provide evidence for a dispute
        :param id:
        :param customer_email: Customer Email
        :param customer_name: Customer Name
        :param customer_phone: Customer Phone
        :param service_details: Details of service involved
        :param kwargs:
        :return:
        """
        data = {'customer_email': customer_email, 'customer_name': customer_name, 'customer_phone': customer_phone,
                'service_detail': service_details, **kwargs}
        return await self.post(url=self.url(f"{id}/evidence"), json=data)

    async def get_upload_url(self, *, id: str, upload_filename: str):
        """
        Get URL to upload a dispute evidence.
        :param id: Dispute Id
        :param upload_filename: The file name, with its extension, that you want to upload. e.g filename.pdf
        :return:
        """
        return await self.get(url=self.url(f"{id}/upload_url"), params={"upload_filename", upload_filename})

    async def resolve(self, *, id: str, resolution: str, message: str, refund_amount: int, uploaded_filename: str, **kwargs):
        """

        :param id: Dispute Id
        :param resolution: Dispute resolution. Accepted values: { merchant-accepted | declined }.
        :param message: Reason for resolving
        :param refund_amount: the amount to refund, in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR
        :param uploaded_filename: filename of attachment returned via response from upload url(GET /dispute/:id/upload_url)
        :param kwargs:
        :return:
        """
        data = {'resolution': resolution, 'message': message, 'refund_amount': refund_amount, 'uploaded_filename': uploaded_filename, **kwargs}
        return await self.put(url=self.url(f"{id}/resolve"), json=data)

    async def export(self, *, from_: date, to: date, **kwargs):
        """
        Export disputes available on your integration
        :param from_: A timestamp from which to start listing dispute e.g. 2016-09-21
        :param to: A timestamp at which to stop listing dispute e.g. 2016-09-21
        :param kwargs:
        :return:
        """
        return await self.get(url=self.url("export"), params={'from': from_, 'to': to, **kwargs})
