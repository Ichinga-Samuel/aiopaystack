
class TransferControl:

    def __init__(self, req):
        self.req = req

    async def check_balance(self):
        """

        :return:
        """
        endpoint = 'balance'
        return await self.req.get(endpoint=endpoint)

    async def check_balance_ledger(self):
        """

        :return:
        """
        endpoint = 'balance/ledger'
        return await self.req.get(endpoint=endpoint)

    async def resend_otp(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        endpoint = "transfer/resend_otp"
        return await self.req.post(endpoint=endpoint, json=kwargs)

    async def disable_otp(self):
        """

        :return:
        """
        endpoint = "transfer/disable_otp"
        return await self.req.post(endpoint=endpoint)

    async def finalize_disable_otp(self, *, otp):
        """
        :param otp:
        :return:
        """
        endpoint = "transfer/disable_otp_finalize"
        return await self.req.post(endpoint=endpoint, json={'otp': otp})

    async def enable_otp(self):
        """

        :return:
        """
        endpoint = "transfer/enable_otp"
        return await self.req.post(endpoint=endpoint)