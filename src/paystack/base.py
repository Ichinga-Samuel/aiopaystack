from typing import TypedDict, NamedTuple
from json.decoder import JSONDecodeError
from logging import getLogger

from httpx import AsyncClient

from .paystack import Paystack

Response = TypedDict('Response', {'status_code': int, 'status': bool, 'message': str, 'data': dict})

Session = NamedTuple("Session", (('status', bool), ('client', AsyncClient | None)))

logger = getLogger()


class Base:
    def __init__(self):
        self.__base = Paystack()
        self.__session = Session(False, None)

    @property
    def __client(self):
        return self.__base.async_client

    async def __aenter__(self) -> 'Base':
        self.__session = Session(True, self.__client)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.__session.client.aclose()
        self.__session = Session(False, None)

    async def __request(self, *, method: str, url: str, **kwargs):
        res = await self.__session.client.request(method, url, **kwargs)
        return self.__get_response(res)

    async def post(self, *, url, **kwargs) -> Response:
        if self.__session.status:
            return await self.__request(method='post', url=url, headers={"Content-type": "application/json"}, **kwargs)

        async with self.__client as client:
            res = await client.post(url, headers={"Content-type": "application/json"}, **kwargs)
            return self.__get_response(res)

    async def get(self, *, url, **kwargs) -> Response:
        if self.__session.status:
            return await self.__request(method='get', url=url, **kwargs)

        async with self.__client as client:
            res = await client.get(url, **kwargs)
            return self.__get_response(res)

    async def delete(self, *, url, **kwargs):
        if self.__session.status:
            return await self.__request(method='delete', url=url, **kwargs)

        async with self.__client as client:
            res = await client.delete(url, **kwargs)
            return self.__get_response(res)

    async def put(self, *, url, **kwargs):
        if self.__session.status:
            return await self.__request(method='put', url=url, headers={"Content-type": "application/json"}, **kwargs)

        async with self.__client as client:
            res = await client.put(url, headers={"Content-type": "application/json"}, **kwargs)
            return self.__get_response(res)

    @staticmethod
    def __get_response(res) -> Response:
        try:
            response = res.json()
            response['status_code'] = res.status_code
            response.setdefault('message', "")
            response.setdefault('status', res.status_code == 200)
            response.setdefault('data', {})
            return response
        except JSONDecodeError:
            logger.error(res.reason_phrase)
            return {'status': False, 'message': "", 'status_code': res.status_code, 'data': {}}
