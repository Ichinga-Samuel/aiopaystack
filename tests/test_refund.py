from paystack import Refund

from . import BaseTest


class TestRefund(BaseTest):

    async def test_refund(self):
        async with Refund() as refund:
            res = await refund.create(transaction="1641")
            assert res['message'] != ""

            res = await refund.list(reference="1234", currency="NGN")
            assert res['status'] is True

            res = await refund.fetch(reference="1234")
            assert res['message'] != ""
