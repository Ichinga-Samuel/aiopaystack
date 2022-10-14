
class Misc:

    def __init__(self, req):
        self.req = req

    async def list_banks(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        endpoint = 'bank'
        return await self.req.get(endpoint=endpoint, params=kwargs) if kwargs else await self.req.get(endpoint=endpoint)

    async def list_providers(self):
        """

        :return:
        """
        endpoint = 'bank'
        return await self.req.get(endpoint=endpoint, params=dict(pay_with_bank_transfer=True))

    async def list_countries(self):
        """

        :return:
        """
        endpoint = 'country'
        return await self.req.get(endpoint=endpoint)

    async def list_states(self, *, country):
        """
        :param country:
        :return:
        """
        endpoint = 'address_verification/states'
        return await self.req.get(endpoint=endpoint, params={'country': country})
