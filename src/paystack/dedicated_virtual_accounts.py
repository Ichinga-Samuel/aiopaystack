from .base import Base


class DedicatedVirtualAccount(Base):
    """
    The Dedicated Virtual Account API enables Nigerian merchants to manage unique payment accounts of their customers.
    """
    def __init__(self):
        super().__init__()
        url = "/dedicated_account/{}"
        self.url = url.format
        
    async def create(self, *, customer: str, **kwargs):
        """
        Create a dedicated virtual account and assign to a customer
        :param customer: Customer ID or code
        :param kwargs:
        :return: Response
        """
        data = {'customer': customer, **kwargs}
        return await self.post(url=self.url(""), json=data)

    async def assign(self, email: str, first_name: str, last_name: str, phone: str, preferred_bank: str, country: str, **kwargs):
        """
        With this endpoint, you can create a customer, validate the customer, and assign a DVA to the customer.
        :param email: Customer email address
        :param first_name: Customer first name
        :param last_name: Customer last name
        :param phone: Customer phone number
        :param preferred_bank: The bank slug for preferred bank. To get a list of available banks, use the List Providers endpoint
        :param country: Currently accepts NG only
        :param kwargs: Optional parameters
        :return:
        """
        data = {'email': email, 'first_name': first_name, 'last_name': last_name,'phone': phone, 'country': country, 'preferred_bank': preferred_bank,
                **kwargs}
        return await self.post(url=self.url('assign'), json=data)

    async def list(self, active: bool = True, currency: str = "NGN", **kwargs):
        """
        List dedicated virtual accounts available on your integration.
        :param active: Status of the dedicated virtual account
        :param currency: The currency of the dedicated virtual account. Only NGN is currently allowed
        :param kwargs: Optional parameters
        :return: Response
        """
        params = {'active': active, 'currency': currency, **kwargs}
        return await self.get(url=self.url(""), params=params)

    async def fetch(self, *, dedicated_account_id):
        """
        Get details of a dedicated virtual account on your integration.
        :param dedicated_account_id: ID of dedicated virtual account
        :return: Response
        """
        return await self.get(url=self.url(f"{dedicated_account_id}"))

    async def deactivate(self, *, dedicated_account_id):
        """
        Deactivate a dedicated virtual account on your integration.
        :param dedicated_account_id: ID of dedicated virtual account
        :return: Response
        """
        return await self.delete(url=self.url(f"{dedicated_account_id}"))

    async def split(self, customer: str, **kwargs):
        """
        Split a dedicated virtual account transaction with one or more accounts
        :param customer: Customer ID or code
        :param kwargs:
        :return: Response
        """
        data = {'customer': customer, **kwargs}
        return await self.post(url=self.url("split"), json=data)

    async def requery(self, *, account_number: str, provider_slug: str, **kwargs):
        """
        Requery Dedicated Virtual Account for new transactions
        :param account_number: Virtual account number to requery
        :param provider_slug: The bank's slug in lowercase, without spaces e.g. wema-bank
        :param kwargs:
        :return: Response
        """
        params = {'account_number': account_number, 'provider_slug': provider_slug, **kwargs}
        return await self.get(url=self.url("requery"), params=params)

    async def remove_split(self, *, account_number: str):
        """
        If you've previously set up split payment for transactions on a dedicated virtual account, you can remove
        it with this endpoint
        :param account_number: Dedicated virtual account number
        :return: Response
        """
        data = {"account_number": account_number}
        return await self.delete(url=self.url("split"), params=data)

    async def fetch_providers(self):
        """
        Get available bank providers for a dedicated virtual account
        :return: Response
        """
        return await self.get(url=self.url("available_providers"))
