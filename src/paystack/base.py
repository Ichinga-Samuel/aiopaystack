import json
from urllib.parse import urlencode
from typing import TypedDict, Literal
from json.decoder import JSONDecodeError
from http.client import HTTPSConnection, HTTPResponse
import asyncio

from .paystack import Paystack

Response = TypedDict('Response', {'status_code': int, 'status': bool, 'message': str, 'data': dict})
Currency = Literal['NGN', 'GHS', 'ZAR', 'USD']


class Base:
    def __init__(self):
        """
        Attributes:
            base (Paystack): Paystack instance.
            session (bool): session is true when class is used as a context manager. False otherwise.
        """
        self.base = Paystack()
        self._client: None | HTTPSConnection = None

    @property
    def client(self) -> HTTPSConnection:
        self._client = self._client if self._client is not None else self.base.client
        return self._client

    @client.setter
    def client(self, conn: HTTPSConnection | None):
        self._client = conn

    async def __aenter__(self) -> 'Base':
        self.client = self.base.client
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        if self._client:
            self._client.close()
            self._client = None

    async def request(self, *, method: str, url: str, **kwargs) -> Response:
        """
        :param method: HTTP method
        :param url: URL to request
        :param kwargs: optional params of request body as keyword arguments
        :return: json data from paystack API as a dict
        """
        if method in ('POST', 'PUT'):
            self.base.headers |= {"Content-type": "application/json"}
        self.base.headers |= kwargs.get('headers', {})
        body = json.dumps(kwargs.get('json', None))
        query = urlencode(kwargs.get('params', {}))
        url += f'?{query}'
        await asyncio.to_thread(self.client.request, method=method, url=url, headers=self.base.headers, body=body)
        res = await asyncio.to_thread(self.client.getresponse)
        return self.response(res)

    async def post(self, *, url, **kwargs) -> Response:
        return await self.request(method='POST', url=url, **kwargs)

    async def get(self, *, url, **kwargs) -> Response:
        return await self.request(method='GET', url=url, **kwargs)

    async def delete(self, *, url, **kwargs) -> Response:
        return await self.request(method='DELETE', url=url, **kwargs)

    async def put(self, *, url, **kwargs) -> Response:
        return await self.request(method='PUT', url=url, **kwargs)

    @staticmethod
    def response(res: HTTPResponse) -> Response:
        try:
            resp = res.read().decode('utf-8')
            response = json.loads(resp)
            response['status_code'] = res.status
            response.setdefault('message', "")
            response.setdefault('status', res.status == 200)
            response.setdefault('data', {})
            return response
        except JSONDecodeError:
            return {'status': False, 'message': res.reason, 'status_code': res.status_code, 'data': {}}
