from paystack import TransactionSplits
from . import BaseTest, transaction_splits as splits


class TestTransactionSplits(BaseTest):

    async def tests(self, splits):
        async with TransactionSplits() as trans_splits:

            # Test Splits Creation
            res = await trans_splits.create(**splits)
            data = res['data']
            splits |= data
            assert data['total_subaccounts'] == 2

            # Test List Splits
            res = await trans_splits.list(name="", active=False)
            assert res['status'] is True

            # Test Fetch Splits
            res = await trans_splits.fetch(id=splits['id'])
            assert splits['id'] == res['data']['id']

            # Test Splits Update
            res = await trans_splits.update(id=splits['id'], name="Test Splits", active=False)
            splits |= res['data']
            assert res['data']['name'] == 'Test Splits'

            # Test Add Subaccount
            res = await trans_splits.add_split_subaccount(id=splits['id'], subaccount="ACCT_29ej5oa80xdeja5", share=5)
            assert res['status'] is True

            # Test Remove Subaccount
            res = await trans_splits.remove_subaccount_from_split(id=splits['id'], subaccount="ACCT_29ej5oa80xdeja5")
            assert res['status'] is True
