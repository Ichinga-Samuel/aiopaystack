from paystack.transactions import Transactions

from . import BaseTest
from .fixtures import init


class TestTransaction(BaseTest):
    transaction = Transactions()

    async def test_initialize(self, init):
        res = await self.transaction.initialize(**init)
        assert res['status'] is True
