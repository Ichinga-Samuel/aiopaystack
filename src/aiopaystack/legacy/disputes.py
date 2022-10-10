
class Dispute:

    def __init__(self, req):
        self.req = req

    async def list(self, **kwargs):
        """

        :return:
        """
        endpoint = "dispute"
        return await self.req.get(endpoint=endpoint, params=kwargs) if kwargs else await self.req.get(endpoint=endpoint)

    async def fetch(self, *, id_):
        """

        :param id_:
        :return:
        """
        endpoint = f"dispute/{id_}"
        return await self.req.get(endpoint=endpoint)

    async def transaction_disputes(self, *, id_):
        """

        :param id_:
        :return:
        """
        endpoint = f"dispute/transaction/{id_}"
        return await self.req.get(endpoint=endpoint)

    async def update(self, *, id_, **kwargs):
        """

        :param id_:
        :kwargs:
        :return:
        """
        endpoint = f"dispute/{id_}"
        return await self.req.put(endpoint=endpoint, json=kwargs)

    async def add_evidence(self, *, id_, **kwargs):
        """

        :param id_:
        :kwargs:
        :return:
        """
        endpoint = f"dispute/{id_}/evidence"
        return await self.req.post(endpoint=endpoint, json=kwargs)

    async def upload_url(self, *, id_, upload_filename):
        """

        :param upload_filename:
        :param id_:
        :return:
        """
        endpoint = f"dispute/{id_}/upload_url"
        return await self.req.get(endpoint=endpoint, params={"upload_filename", upload_filename})

    async def resolve(self, *, id_, **kwargs):
        """

        :param id_:
        :param kwargs:
        :return:
        """
        endpoint = f"dispute/{id_}/resolve"
        return await self.req.put(endpoint=endpoint, json=kwargs)

    async def export(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        endpoint = "dispute/export"
        return await self.req.get(endpoint=endpoint, params=kwargs) if kwargs else await self.req.get(endpoint=endpoint)
