
class Page:

    def __init__(self, req):
        self.req = req

    async def create(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        endpoint = "page"
        return await self.req.post(endpoint=endpoint, json=kwargs)

    async def list(self, **kwargs):
        """

        :return:
        """
        endpoint = "page"
        return await self.req.get(endpoint=endpoint, params=kwargs) if kwargs else await self.req.get(endpoint=endpoint)

    async def fetch(self, *, slug):
        """

        :param slug:
        :return:
        """
        endpoint = f"page/{slug}"
        return await self.req.get(endpoint=endpoint)

    async def update(self, *, slug, **kwargs):
        """

        :param slug:
        :param kwargs:
        :return:
        """
        endpoint = f"page/{slug}"
        return await self.req.put(endpoint=endpoint, json=kwargs)

    async def is_slug_available(self, *, slug):
        """

        :param slug:
        :return:
        """
        endpoint = f"page/check_slug_availability/{slug}"
        return await self.req.get(endpoint=endpoint)

    async def add_products(self, *, page_id, **kwargs):
        """

        :param page_id:
        :param kwargs:
        :return:
        """
        endpoint = f"page/{page_id}/product"
        return await self.req.post(endpoint=endpoint, json=kwargs)
