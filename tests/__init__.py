import pytest
import os
from paystack import Paystack
from .fixtures import *


@pytest.mark.asyncio
class BaseTest:
    Paystack(secret_key=os.getenv('PAY_STACK_SECRET_KEY'))
