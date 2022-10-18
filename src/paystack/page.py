from datetime import datetime
from .base import Base

class PaymentPages(Base):
    """
    The Payment Pages API provides a quick and secure way to collect payment for products.
    """
    def __init__(self):
        super().__init__()
        url = '/page/{}'
        self.url = url.format

    async def create(self, *, name: str, **kwargs):
       """
       Create a payment page on your integration
       :param name: Name of page
       :param kwargs:
       :return: Response
       """
       data = {'name': name, **kwargs}
       return await self.post(url=self.url(""), json=data)

    async def list(self, *, perPage: int = 50, page: int = 1,  from_: datetime | None = None, to: datetime | None = None):
        """
        List payment pages available on your integration.
        :param perPage: Specify how many records you want to retrieve per page. If not specify we use a default value of 50.
        :param page: Specify exactly what page you want to retrieve. If not specify we use a default value of 1.
        :param from_: A timestamp from which to start listing page e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
        :param to: A timestamp at which to stop listing page e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
        :return: Response
        """

        params = {key: value for key, value in (('perPage', perPage), ('page', page), ('from', from_), ('to', to)) if value}
        return await self.get(url=self.url(""), params=params)

    async def fetch(self, *, id_or_slug):
        """
        Get details of a payment page on your integration.
        :param id_or_slug: The page ID or slug you want to fetch
        :return: Response
        """
        params = {'id_or_slug': id_or_slug}
        return await self.get(url=self.url(f"{id_or_slug}"), params=params)

    async def update(self, *, id_or_slug: str, name: str, description: str, **kwargs):
        """
        Update a payment page details on your integration
        :param id_or_slug: Page ID or slug
        :param name: Name of page
        :param description: A description for this page
        :param kwargs:
        :return: Response
        """
        params = {'id_or_slug': id_or_slug, 'name': name, 'description': description, **kwargs}
        return await self.get(url=self.url(f"{id_or_slug}"), params=params)

    async def is_slug_available(self, *, slug):
        """
        Check the availability of a slug for a payment page.
        :param slug: URL slug to be confirmed
        :return: Response
        """
        params = {'slug': slug}
        return await self.get(url=self.url(f"check_slug_availability/{slug}"), params=params)

    async def add_products(self, *, id: int, product: list[dict]):
        """
        Add products to a payment page
        :param id: Id of the payment page
        :param product: Ids of all the products
        :return: Response
        """
        data = {'id': id, 'product': product}
        return await self.post(url=self.url("product"), json=data)
