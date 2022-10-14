import pytest


@pytest.fixture(scope='session')
def init():
    return {'email': "ichingasamuel@gmail.com", 'amount': "50000", "kwargs": {}}
