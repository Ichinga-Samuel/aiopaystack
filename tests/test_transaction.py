from paystack import Transactions

from . import BaseTest
from .fixtures import init, transaction_reference, transaction_id, transaction_details, verify_transaction
# create_charge, charge_authorization


class TestTransaction(BaseTest):
    transaction = Transactions()

    async def test_initialize(self, init):
        res = await self.transaction.initialize(**init)
        assert res['status'] is True

    async def test_list(self):
        res = await self.transaction.list()
        assert res['status'] is True

    async def test_verify(self, transaction_reference):
        ref = await transaction_reference
        res = await self.transaction.verify(reference=ref)
        assert res['status'] is True

    async def test_fetch(self, transaction_id):
        _id = await transaction_id
        res = await self.transaction.fetch(id=_id)
        assert res['status'] is True

    # async def test_charge_authorization(self, charge_authorization):
    #     data = await charge_authorization
    #     res = await self.transaction.charge_authorization(**data)
    #     assert res['status'] is True

    # async def test_check_authorization(self):
    #     res = await self.transaction.check_authorization(**{"email": "customer@email.com", "amount": "20000", "authorization_code": "AUTH_72btv547"})
    #     assert res['status'] is True

    async def test_timeline(self, transaction_details):
        res = await transaction_details
        res = await self.transaction.view_transaction_timeline(id_or_reference=res['data']['reference'])
        assert res['status'] is True

    async def test_totals(self):
        res = await self.transaction.transaction_totals()
        assert res['status'] is True

    async def test_export_transaction(self):
        res = await self.transaction.export_transactions()
        assert res['status'] is True

    # async def test_partial_debit(self):
    #     res = await self.transaction.partial_debit(**{"email": "customer@email.com", "amount": "20000", "authorization_code": "AUTH_72btv547"})
    #     assert res['status'] is True