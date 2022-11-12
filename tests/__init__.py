import asyncio
from pprint import pprint as pp

import pytest

from paystack import Paystack, Transactions
from .fixtures import *


@pytest.mark.asyncio
class BaseTest:
    Paystack(secret_key="sk_test_0a246ef179dc841f42d20959bebdd790f69605d8")


async def che():
    Paystack(secret_key="sk_test_0a246ef179dc841f42d20959bebdd790f69605d8")
    init = {'email': "ichingasamuel@gmail.com", 'amount': "50000", "kwargs": {}}
    async with Transactions() as trans:
        res = await trans.initialize(**init)
        res = await trans.verify(reference=res['data']['reference'])
    # res = Transactions()
    # re = await res.initialize(**init)
    # re = await res.verify(reference=re['data']['reference'])
    # pp(res)

# asyncio.run(che())
