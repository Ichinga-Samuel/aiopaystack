import functools
import random

import pytest


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
def customers():
    return [
        {
            'first_name': 'Ade',
            'last_name': 'Wale',
            'middle_name': 'Segun',
            'email': 'adewale@email.com',
            'phone': "+234123456789",
            'preferred_bank': 'test-bank',
            'country': 'NG',
            'type': 'bank_account',
            'account_number': '0123456789',
            'bvn': '20012345677',
            'bank_code': '007',
            'metadata': {
                'available': 'true'}
        },
        {
            'first_name': 'Barko',
            'last_name': 'Sarki',
            'email': 'barkosarki@gmail.com',
            'phone': "+234123456798",
            'metadata': {
                'available': 'true'}

        }
    ]


@pytest.fixture(scope='session')
def customer(customers):
    return customers[0]


@pytest.fixture(scope='session')
def transaction(customer):
    return {'email': customer['email'], 'amount': '20000'}


@pytest.fixture(scope='session')
def recipient():
    return {"type": "nuban", "name": "Tolu Robert", "account_number": "0100000001", "bank_code": "063", "currency": "NGN"}


@pytest.fixture(scope='session')
def recipients():
    return {"batch": [
        {
            "type": "nuban",
            "name": "Habenero Mundane",
            "account_number": "0123456789",
            "bank_code": "033",
            "currency": "NGN"
        },
        {
            "type": "nuban",
            "name": "Soft Merry",
            "account_number": "9876543231",
            "bank_code": "50211",
            "currency": "NGN"
        }]
    }





@pytest.fixture(scope='session')
def init_charge():
    return {'email': 'customer@email.com', 'amount': '50000', 'bank': {'code': "057", 'account_number': "0987654321"}, 'birthday': "1967-12-23"}



@pytest.fixture(scope="session")
def charges():
    return [
        {"authorization": "AUTH_ncx8hews93", "amount": 2500, "reference": "dam1266638dhhd"},
        {"authorization": "AUTH_xfuz7dy4b9", "amount": 1500, "reference": "dam1266638dhhe"}
    ]


@pytest.fixture(scope="session")
def validate_account():
    return {
        "bank_code": "632005",
        "country_code": "ZA",
        "account_number": "0123456789",
        "account_name": "Ann Bron",
        "account_type": "personal",
        "document_type": "identityNumber",
        "document_number": "1234567890123"
    }


@pytest.fixture(scope="session")
def initiate_transfer():
    return {"source": "balance", "reason": "Calm down", "amount": 3794800, "recipient": "RCP_gx2wn530m0i3w3m"}


@pytest.fixture(scope="session")
def bulk_transfer():
    return {"currency": "NGN",
            "source": "balance",
            "transfers": [{
                "amount": 50000,
                "recipient": "RCP_db342dvqvz9qcrn",
                "reference": "ref_943899312"
            },
                {
                    "amount": 50000,
                    "recipient": "RCP_db342dvqvz9qcrn",
                    "reference": "ref_943889313"
                }]
            }


@pytest.fixture(scope="session")
def transaction_splits():
    return {"name": "Test Split",
            "type": "percentage",
            "currency": "NGN",
            "subaccounts": [{
                "subaccount": "ACCT_clmnn0r1rw7mbwi",
                "share": 20
            },
                {
                    "subaccount": "ACCT_xo65xntj0n21zmr",
                    "share": 50
                }],
            "bearer_type": "all",
            "bearer_subaccount": None
            }


@pytest.fixture(scope="session")
def subaccount():
    return {"business_name": "Sunshine Studios", "settlement_bank": "044", "account_number": "0193274682", "percentage_charge": 18.2}


@pytest.fixture(scope="session")
def invoice():
    return {"description": "a test invoice",
            "line_items": [
                {"name": "item 1", "amount": 20000},
                {"name": "item 2", "amount": 20000}
            ],
            "tax": [
                {"name": "VAT", "amount": 2000}
            ],
            "customer": "CUS_xwaj0txjryg393b",
            "due_date": "2020-07-08"
            }


@pytest.fixture(scope="session")
def dvac(customer):
    return customer


@pytest.fixture(scope="session")
def split_dva():
    return {"customer": 481193, "preferred_bank": "wema-bank", "split_code": "SPL_e7jnRLtzla"}
