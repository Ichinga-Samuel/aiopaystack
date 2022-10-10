import pytest

from aiopaystack.transactions import Transactions

from . import BaseTest


@pytest.fixture(scope='class')
def init():
    return {'email': "ichingasamuel@gmail.com", 'amount': "50000", "kwargs": {}}


class TestTransaction(BaseTest):
    transaction = Transactions()

    async def test_initialize(self, init):
        res = await self.transaction.initialize(**init)
        assert res['status'] is True
