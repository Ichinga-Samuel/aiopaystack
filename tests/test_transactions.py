from paystack import Transactions

from . import BaseTest, init


class TestTransaction(BaseTest):
    async def tests(self, init):
        async with Transactions() as transactions:
            res = await transactions.initialize(**init)
            data = res['data']
            assert res['status'] is True

            res = await transactions.list()
            assert res['status'] is True

            res = await transactions.verify(reference=data['reference'])
            data = res['data']
            assert res['status'] is True

            res = await transactions.fetch(id=data['id'])
            assert res['status'] is True

            res = await transactions.charge_authorization(email=init['email'], amount=init['amount'], authorization_code="AUTH_72btv547")
            assert res['message'] != ""

            res = await transactions.check_authorization(email=init['email'], amount=init['amount'], authorization_code="AUTH_72btv547")
            assert res['message'] != ""

            res = await transactions.view_transaction_timeline(id_or_reference=data['reference'])
            assert res['status'] is True

            res = await transactions.transaction_totals()
            assert res['status'] is True

            res = await transactions.export_transactions()
            assert res['status'] is True

            res = await transactions.partial_debit(email=init['email'], amount=init['amount'], authorization_code="AUTH_72btv547", currency="NGN")
            assert res['message'] != ""
