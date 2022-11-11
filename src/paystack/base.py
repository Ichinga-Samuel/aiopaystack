from typing import TypedDict

from httpx import AsyncClient
from .paystack import Paystack


Response = TypedDict('Response', {'status_code': int, 'status': bool, 'message': str, 'data': dict})


class Base:
    def __init__(self):
        self.base = Paystack()
        self.session = False
        self._client: AsyncClient | None = None

    @property
    def client(self):
        return self.base.client

    async def __aenter__(self) -> 'Base':
        self.session = True
        self._client = self.client
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self._client.aclose()
        self.session = False
        self._client = None

    async def request(self, *, method: str, url: str, **kwargs):
        res = await self._client.request(method, url, **kwargs)
        response = res.json()
        response['status_code'] = res.status_code
        response.setdefault('data', {})
        return response

    async def post(self, *, url, **kwargs) -> Response:
        if self.session:
            return await self.request(method='post', url=url, headers={"Content-type": "application/json"}, **kwargs)

        async with self.client as client:
            res = await client.post(url, headers={"Content-type": "application/json"}, **kwargs)
            response = res.json()
            response['status_code'] = res.status_code
            response.setdefault('data', {})
            return response

    async def get(self, *, url, **kwargs) -> Response:
        if self.session:
            return await self.request(method='get', url=url, **kwargs)

        async with self.client as client:
            res = await client.get(url, **kwargs)
            response = res.json()
            response['status_code'] = res.status_code
            response.setdefault('data', {})
            return response

    async def delete(self, *, url, **kwargs):
        if self.session:
            return await self.request(method='delete', url=url, **kwargs)

        async with self.client as client:
            res = await client.delete(url, **kwargs)
            response = res.json()
            response['status_code'] = res.status_code
            response.setdefault('data', {})
            return response

    async def put(self, *, url, **kwargs):
        if self.session:
            return await self.request(method='put', url=url, headers={"Content-type": "application/json"}, **kwargs)

        async with self.client as client:
            res = await client.put(url, headers={"Content-type": "application/json"}, **kwargs)
            response = res.json()
            response['status_code'] = res.status_code
            response.setdefault('data', {})
            return response
