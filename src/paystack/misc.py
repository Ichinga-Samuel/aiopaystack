from .base import Base


class Miscellaneous(Base):
    """
    The Miscellaneous API are supporting APIs that can be used to provide more details to other APIs
    """

    def __init__(self):
        super().__init__()
        url = "/bank/{}"
        self.url = url.format

    async def list_banks(self, *, country: str = "nigeria", use_cursor: bool = True, perPage: int = 50, **kwargs):
        """
        Get a list of all supported banks and their properties
        :param country: The country from which to obtain the list of supported banks. e.g country=ghana or country=nigeria
        :param use_cursor: Flag to enable cursor pagination on the endpoint
        :param perPage: The number of objects to return per page. Defaults to 50, and limited to 100 records per page.
        :param kwargs:
        :return: Response
        """
        params = {'country': country, 'use_cursor': use_cursor, 'perPage': perPage, **kwargs}
        return await self.get(url=self.url(""), params=params)

    async def list_providers(self):
        """
        :return: Response
        """
        return await self.get(url=self.url(""), params=dict(pay_with_bank_transfer=True))

    async def list_countries(self):
        """
        Gets a list of Countries that Paystack currently supports
        :return: Response
        """
        return await self.get(url=self.url(""))

    async def list_states(self, *, country: str):
        """
        Get a list of states for a country for address verification.
        :param country: The country code of the states to list. It is gotten after the charge request.
        :return: Response
        """
        params = {'country': country}
        return await self.get(url="address_verification/states", params=params)
