from paystack import ApplePay

from . import BaseTest


class TestApplePay(BaseTest):

    async def tests(self):
        async with ApplePay() as apple:
            res = await apple.register(domainName="apple.com")
            assert res['message'] != ""

            res = await apple.list()
            assert res['status'] is True

            res = await apple.unregister(domainName="apple.com")
            assert res['message'] != ""
