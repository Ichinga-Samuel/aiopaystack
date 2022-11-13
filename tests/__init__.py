import pytest

from paystack import Paystack
from .fixtures import *


@pytest.mark.asyncio
class BaseTest:
    Paystack(secret_key="sk_test_0a246ef179dc841f42d20959bebdd790f69605d8")
