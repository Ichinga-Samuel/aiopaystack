from paystack import Verification

from . import BaseTest, validate_account


class TestVerification(BaseTest):

    async def tests(self, validate_account):
        async with Verification() as verify:
            res = await verify.resolve_account_number(account_number="0022728151", bank_code="063")
            assert res['message'] != ""

            res = await verify.validate_account(**validate_account)
            assert res['message'] != ""

            res = await verify.resolve_card_bin(bin="539983")
            assert res['status'] is True
