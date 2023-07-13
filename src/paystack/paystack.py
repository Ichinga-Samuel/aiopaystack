import os
from http.client import HTTPSConnection


class Paystack:

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, *, secret_key=""):
        self.secret_key = secret_key or os.getenv('PAY_STACK_SECRET_KEY') or getattr(self, 'secret_key', '')
        self.headers = {'Authorization': f'Bearer {self.secret_key}'}

    @property
    def client(self) -> HTTPSConnection:
        client = HTTPSConnection('api.paystack.co')
        return client
