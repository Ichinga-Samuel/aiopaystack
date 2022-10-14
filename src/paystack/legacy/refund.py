
class Refund:

    def __init__(self, req):
        self.req = req

    async def create(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        endpoint = "refund"
        return await self.req.post(endpoint=endpoint, json=kwargs)

    async def list(self, **kwargs):
        """

        :return:
        """
        endpoint = "refund"
        return await self.req.get(endpoint=endpoint, params=kwargs) if kwargs else await self.req.get(endpoint=endpoint)

    async def fetch(self, *, ref):
        """

        :param ref:
        :return:
        """
        endpoint = f"refund/{ref}"
        return await self.req.get(endpoint=endpoint)
