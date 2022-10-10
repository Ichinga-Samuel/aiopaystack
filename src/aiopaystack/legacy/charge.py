
class Charge:

    def __init__(self, req):
        self.req = req

    async def start_charge(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        endpoint = 'charge'
        return await self.req.post(endpoint=endpoint, json=kwargs)

    async def submit_pin(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        endpoint = "charge/submit_pin"
        return await self.req.post(endpoint=endpoint, json=kwargs)

    async def submit_otp(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        endpoint = 'charge/submit_otp'
        return await self.req.post(endpoint=endpoint, json=kwargs)

    async def submit_phone(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        endpoint = 'charge/submit_phone'
        return await self.req.post(endpoint=endpoint, json=kwargs)

    async def submit_birthday(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        endpoint = 'charge/submit_birthday'
        return await self.req.post(endpoint=endpoint, json=kwargs)

    async def submit_address(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        endpoint = 'charge/submit_address'
        return await self.req.post(endpoint=endpoint, json=kwargs)

    async def check_pending(self, *, ref):
        """

        :param ref:
        :return:
        """
        endpoint = f'charge/{ref}'
        return await self.req.get(endpoint=endpoint)
