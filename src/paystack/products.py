from datetime import datetime

from .base import Base


class Products(Base):
    """
    The Products API allows you create and manage inventories on your integration
    """
    def __init__(self):
        super().__init__()
        url = "/product/{}"
        self.url = url.format

    async def create(self, *, name: str, description: str, price: int, currency: str, **kwargs):
        """
        Create a product on your integration
        :param name: Name of product
        :param description: A description for this product
        :param price: Price should be in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR
        :param currency: Currency in which price is set. Allowed values are: NGN, GHS, ZAR or USD
        :kwargs:
        :return: Response
        """
        data = {'name': name, 'description': description, 'price': price, 'currency': currency, **kwargs}
        return await self.post(url=self.url(""), json=data)

    async def list(self, perPage: int = 50, page: int = 1, from_: datetime | None | str = None, to: datetime | None | str = None):
        """
        List products available on your integration.
        :param perPage: Specify how many records you want to retrieve per page. If not specify we use a default value of 50.
        :param page: Specify exactly what page you want to retrieve. If not specify we use a default value of 1.
        :param from_: A timestamp from which to start listing product e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
        :param to: A timestamp at which to stop listing product e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
        :return: Response
        """
        params = {key: value for key, value in (('perPage', perPage), ('page', page), ('from', from_), ('to', to))}
        return await self.get(url=self.url(""), params=params)

    async def fetch(self, *, id: str):
        """
        Get details of a product on your integration.
        :param id: The product ID you want to fetch
        :return: Response
        """
        return await self.get(url=self.url(f"{id}"))

    async def update(self, *, id: str, name: str, description: str, price: int, currency: str, **kwargs):
        """
        Update a product details on your integration
        :param id: Product ID
        :param name: Name of product
        :param description: A description for this product
        :param price: Price should be in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR
        :param currency: Currency in which price is set. Allowed values are: NGN, GHS, ZAR or USD
        :param kwargs:
        :return: Response
        """
        data = {'name': name, 'description': description, 'price': price, 'currency': currency, **kwargs}
        return await self.put(url=self.url(f"{id}"), json=data)
