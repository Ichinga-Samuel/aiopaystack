import pytest

from aiopaystack.paystack import Paystack


@pytest.mark.asyncio
class BaseTest:
    paystack = Paystack(secret_key="sk_test_0a246ef179dc841f42d20959bebdd790f69605d8")
