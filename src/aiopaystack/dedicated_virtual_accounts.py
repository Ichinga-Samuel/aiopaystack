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
        :param customer:
        :param kwargs:
        :return:
        """
        
        return await self.post(url=self.url(""), json={'customer': customer, **kwargs})

    async def list(self, active: bool, currency: str = "NGN", **kwargs):
        """
        List dedicated virtual accounts available on your integration.
        :param currency:
        :param active:
        :param kwargs:
        :return:
        """
        return await self.get(url=self.url(""), params={'active': active, 'currency': currency, **kwargs})

    async def fetch(self, *, dedicated_account_id):
        """
        Get details of a dedicated virtual account on your integration.
        :param dedicated_account_id: ID of dedicated virtual account
        :return:
        """
        return await self.get(url=self.url(f"{dedicated_account_id}"))

    async def deactivate(self, *, dedicated_account_id):
        """
        Deactivate a dedicated virtual account on your integration.
        :param dedicated_account_id: ID of dedicated virtual account
        :return:
        """
        
        return await self.delete(url=self.url(f"{dedicated_account_id}"))

    async def split(self, customer: str, **kwargs):
        """
        Split a dedicated virtual account transaction with one or more accounts
        :param customer: Customer ID or code
        :param kwargs:
        :return:
        """
        return await self.post(url=self.url("split"), json={'customer': customer, **kwargs})

    async def requery(self, *, account_number: str, provider_slug: str, **kwargs):
        """
        Requery Dedicated Virtual Account for new transactions
        :param account_number: Virtual account number to requery
        :param provider_slug: The bank's slug in lowercase, without spaces e.g. wema-bank
        :param kwargs:
        :return:
        """
        return self.get(url=self.url("requery"), params={'account_number': account_number, 'provider_slug': provider_slug, **kwargs})

    async def remove_split(self, *, account_number: str):
        """
        If you've previously set up split payment for transactions on a dedicated virtual account, you can remove it with this endpoint
        :param account_number: Dedicated virtual account number
        :return:
        """
        return await self.delete(url=self.url("split"), json={"account_number": account_number})

    async def fetch_providers(self):
        """
        Get available bank providers for a dedicated virtual account
        :return:
        """
        return await self.get(url=self.url("available_providers"))
