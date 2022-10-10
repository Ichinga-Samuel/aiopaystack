
class Verification:

    def __init__(self, req):
        self.req = req

    async def verify_account(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        endpoint = 'bank/resolve'
        return await self.req.get(endpoint=endpoint, params=kwargs)

    async def verify_bvn(self, *, bvn):
        """

        :param bvn:
        :return:
        """
        endpoint = f'bank/resolve_bvn/{bvn}'
        return await self.req.get(endpoint=endpoint)

    async def verify_card_bin(self, *, card_bin):
        """

        :param card_bin:
        :return:
        """
        endpoint = f'decision/bin/{card_bin}'
        return await self.req.get(endpoint=endpoint)

    async def verify_phone_number(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        endpoint = "verifications"
        return await self.req.get(endpoint=endpoint, json=kwargs)

    async def match_bvn(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        endpoint = "bvn/match"
        return await self.req.get(endpoint=endpoint, json=kwargs)
