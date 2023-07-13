from paystack import Transactions
from . import BaseTest, customer, transaction, customers


class TestTransaction(BaseTest):
    async def test_transactions(self, customer, transaction):
        async with Transactions() as trans:
            # Test transaction initialization
            res = await trans.initialize(**transaction)
            data = res['data']
            transaction |= data
            assert res['status'] is True

            # Test transaction verification
            res = await trans.verify(reference=transaction['reference'])
            data = res['data']
            transaction |= data
            assert data['status'] == 'abandoned'

            # Test transaction listing
            res = await trans.list(perPage=50)
            assert res['status'] is True

            # Test transaction fetching
            res = await trans.fetch(id=transaction['id'])
            data = res['data']
            assert transaction['reference'] == data['reference']

            # # Test transaction charging authorization
            res = await trans.charge_authorization(email=transaction['email'], amount=transaction['amount'],
                                                   authorization_code=transaction['access_code'])
            assert res['status'] is False

            # Test transaction timeline viewing
            res = await trans.view_transaction_timeline(id_or_reference=transaction['reference'])
            assert res['status'] is True

            # Test transaction totals
            res = await trans.transaction_totals(perPage=10)
            assert res['status'] is True

            # Test transaction export
            res = await trans.export_transactions()
            assert res['status'] is True

            # Test transaction partial debit
            res = await trans.partial_debit(email=transaction['email'], amount=transaction['amount'],
                                            authorization_code=transaction['access_code'], currency="NGN")
            assert res['status'] is False
