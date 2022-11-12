from paystack import SubAccounts

from . import BaseTest, subaccount


class TestSubAccounts(BaseTest):

    async def tests(self, subaccount):
        async with SubAccounts() as sub:
            res = await sub.create(**subaccount)
            assert res['message'] != ""

            res = await sub.list()
            assert res['status'] is True

            res = await sub.fetch(id_or_code="sub_id")
            assert res['message'] != ""

            res = await sub.update(id_or_code="subid", business_name="The Business", settlement_bank="067", account_number="0193274682")
            assert res['message'] != ""
