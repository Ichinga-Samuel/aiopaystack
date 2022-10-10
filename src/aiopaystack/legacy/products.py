

class Product:

    def __init__(self, req):
        self.req = req

    async def create(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        endpoint = "product"
        return await self.req.post(endpoint=endpoint, json=kwargs)

    async def list(self, **kwargs):
        """

        :return:
        """
        endpoint = "product"
        return await self.req.get(endpoint=endpoint, params=kwargs) if kwargs else await self.req.get(endpoint=endpoint)

    async def fetch(self, *, product_id):
        """

        :param product_id:
        :return:
        """
        endpoint = f"product/{product_id}"
        return await self.req.get(endpoint=endpoint)

    async def update(self, *, product_id, **kwargs):
        """

        :param product_id:
        :param kwargs:
        :return:
        """
        endpoint = f"product/{product_id}"
        return await self.req.put(endpoint=endpoint, json=kwargs)
