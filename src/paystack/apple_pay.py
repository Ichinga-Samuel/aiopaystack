from .base import Base


class ApplePay(Base):
    """
    The Apple Pay API allows you register your application's top-level domain or subdomain
    """

    def __init__(self):
        super().__init__()
        self.url = "/apple-pay/{}".format

    async def register(self, domainName: str):
        """
        Register a top-level domain or subdomain for your Apple Pay integration.
        :param domainName: Domain name to be registered
        :return: Response
        """
        return await self.post(url=self.url('domain'), json={'domainName': domainName})

    async def list(self):
        """
        Lists all registered domains on your integration. Returns an empty array if no domains have been added.
        :return: Response
        """
        return await self.get(url=self.url('domain'))

    async def unregister(self, domainName: str):
        """
        Unregister a top-level domain or subdomain previously used for your Apple Pay integration.
        :param domainName: Domain name to be registered
        :return: Response
        """
        return await self.delete(url=self.url("domain"), params={'domainName': domainName})
