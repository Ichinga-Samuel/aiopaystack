import functools
import random

import pytest

from paystack import Transactions, Charge


class Cacheable:
    def __init__(self, func):
        self.done = False
        self.result = None
        self.func = func
        functools.update_wrapper(self, func)

    def __call__(self, *args, **kwargs):
        if not self.done:
            self.func = self.func(*args, **kwargs)
        return self

    def __await__(self):
        if self.done:
            return self.result
        else:
            self.result = yield from self.func.__await__()
            self.done = True
            return self.result


@pytest.fixture(scope='session')
def init():
    return {'email': "ichingasamuel@gmail.com", 'amount': "50000", "kwargs": {}}


@pytest.fixture(scope='session')
@Cacheable
async def transaction_details():
    init = {'email': "ichingasamuel@gmail.com", 'amount': "50000", "kwargs": {}}
    async with Transactions() as trans:
        return await trans.initialize(**init)


@pytest.fixture(scope='session')
async def verify_transaction(transaction_details):
    res = await transaction_details
    async with Transactions() as trans:
        res = await trans.verify(reference=res['data']['reference'])
        return res


@pytest.fixture(scope='session')
async def transaction_reference(transaction_details):
    res = await transaction_details
    return res['data']['reference']


@pytest.fixture(scope='session')
async def transaction_id(verify_transaction):
    res = await verify_transaction
    return res['data']['id']

#
# @pytest.fixture(scope='session')
# async def charge_authorization(create_charge, init):
#     charge = await create_charge
#     auth = charge['authorization']['authorization_code']
#     data = {**init, "authorization_code": auth}
#     return data


@pytest.fixture(scope='session')
def init_charge():
    return {'email': 'ichingasamuel@gmail.com', 'amount': '50000', 'bank': {'code': "057", 'account_number': "0000000000"}, 'birthday': "1995-12-23"}


@pytest.fixture(scope="session")
def customer():
    seed = list("dfvkdfvnldfkdfffddfhfgjfgmldiejnvfbtgjewnfpclfmsdnkn")
    slice = random.randint(4, 10)
    random.shuffle(seed)
    name = ''.join(seed[0: slice])
    return {'email': f'{name}@gmail.com', 'first_name': 'Samuel', 'last_name': 'Ichinga', 'phone': '+2349037031782'}


@pytest.fixture(scope="session")
def validate_customer():
    return {'email': 'ichingasamuel@gmail.com', 'first_name': 'Samuel', 'last_name': 'Ichinga', 'account_number': '0042926389', 'bvn': '20012345677',
            'bank_code': '067', 'type': 'bank_account', 'country': 'NG'}


@pytest.fixture(scope="session")
def charges():
    return [
      {"authorization": "AUTH_ncx8hews93", "amount": 2500, "reference": "dam1266638dhhd"},
      {"authorization": "AUTH_xfuz7dy4b9", "amount": 1500, "reference": "dam1266638dhhe"}
    ]


# @pytest.fixture(scope='session')
# async def create_charge(init):
#     res = await Charge().create(**init)
#     print(res)
#     return res
