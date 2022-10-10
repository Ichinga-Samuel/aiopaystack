
class BulkCharge:

    def __init__(self, req):
        self.req = req

    async def initiate_bulk_charge(self, *, bulkcharge):
        """
        :param bulkcharge: array of charges
        :return:
        """
        endpoint = 'bulkcharge'
        return await self.req.post(endpoint=endpoint, json=bulkcharge)

    async def list(self, **kwargs):
        """
        if you specify a page number also specify a results per page. eg page=1, perPage=10
        :param kwargs: query parameters as keyword arguments
        :return:
        """
        endpoint = "bulkcharge"
        return await self.req.get(endpoint=endpoint, params=kwargs) if kwargs else await self.req.get(endpoint=endpoint)

    async def fetch_bulk_batch(self, *, code, **kwargs):
        """
        retrieves a specific batch code
        :param code:
        :param kwargs:
        :return:
        """
        endpoint = f"bulkcharge/{code}"
        return await self.req.get(endpoint=endpoint, params=kwargs)

    async def fetch_charges_batch(self, *, code, **kwargs):
        """

        :param code:
        :param kwargs:
        :return:
        """
        endpoint = f"bulkcharge/{code}/charges"
        return await self.req.get(endpoint=endpoint, params=kwargs) if kwargs else await self.req.get(endpoint=endpoint)

    async def pause_bulk_charge(self, *, code):
        """

        :param code:
        :return:
        """
        endpoint = f"bulkcharge/pause/{code}"
        await self.req.get(endpoint=endpoint)

    async def resume_bulk_charge(self, *, code):
        """
        :param code:
        :return:
        """
        endpoint = f"bulkcharge/resume/{code}"
        await self.req.get(endpoint=endpoint)


