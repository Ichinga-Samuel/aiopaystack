from paystack import TransactionSplits

from . import BaseTest, splits


class TestTransactionSplits(BaseTest):

    async def tests(self, splits):
        async with TransactionSplits() as trans_splits:
            res = await trans_splits.create(**splits)
            assert res['message'] != ""

            res = await trans_splits.list(name="split", active=True)
            assert res['status'] is True

            res = await trans_splits.search(name="split", active=True)
            assert res['status'] is True

            res = await trans_splits.fetch(id="split_id")
            assert res['message'] != ""

            res = await trans_splits.update(id="split_id", name="Newman", active=True)
            assert res['message'] != ""

            res = await trans_splits.add_split_subaccount(id="split_id", subaccount="ACCT_hdl8abxl8drhrl3", share=4000)
            assert res['message'] != ""

            res = await trans_splits.remove_subaccount_from_split(id="split_id", subaccount="ACCT_hdl8abxl8drhrl3")
            assert res['message'] != ""
