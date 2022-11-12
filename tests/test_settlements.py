from paystack import Settlements

from . import BaseTest


class TestSettlements(BaseTest):

    async def tests(self):
        async with Settlements() as settle:
            res = await settle.fetch()
            assert res['status'] is True

            res = await settle.fetch_settlement_transactions()
            assert res['status'] is True
