from .base import Base


class Subscriptions(Base):
    """
    The Subscriptions API allows you create and manage recurring payment on your integration
    """

    def __init__(self):
        super().__init__()
        url = "/subscription/"
        self.url = url.format

    async def create(self, *, customer: str, plan: str, authorization: str = "", start_date: str = ""):
        """
        Create a subscription on your integration
        :param customer: Customer's email address or customer code
        :param plan: Plan code
        :param authorization: If customer has multiple authorizations, you can set the desired authorization you wish to use for this subscription
         here. If this is not supplied, the customer's most recent authorization would be used
        :param start_date: Set the date for the first debit. (ISO 8601 format) e.g. 2017-05-16T00:30:13+01:00
        :return: Response
        """
        data = {'customer': customer, 'plan': plan, 'authorization': authorization}
        data.update(start_date=start_date) if start_date else ...
        return await self.post(url=self.url(""), json=data)

    async def list(self, *, perPage: int = 50, page: int = 1, customer: int | None = None, plan: int | None = None):
        """
        List subscriptions available on your integration.
        :param page: Specify exactly what page you want to retrieve. If not specify we use a default value of 1.
        :param perPage: Specify how many records you want to retrieve per page. If not specify we use a default value of 50.
        :param customer: Filter by Customer ID
        :param plan: Filter by Plan ID
        :return: Response
        """
        params = {key: value for key, value in (('perPage', perPage), ('page', page), ('customer', customer), ('plan', plan)) if value}
        return await self.get(url=self.url(""), params=params)

    async def fetch(self, *, id_or_code: str):
        """
        Get details of a subscription on your integration.
        :param id_or_code: The subscription ID or code you want to fetch
        :return: Response
        """
        return await self.get(url=self.url(f"{id_or_code}"))

    async def enable(self, code: str, token: str):
        """
        Enable a subscription on your integration
        :param code: Subscription code
        :param token: Email token
        :return: Response
        """
        data = {'code': code, 'token': token}
        return await self.post(url=self.url("enable"), json=data)

    async def disable(self, *, code: str, token: str):
        """
        Disable a subscription on your integration
        :param code: Subscription code
        :param token: Email token
        :return: Response
        """
        data = {'code': code, 'token': token}
        return await self.post(url=self.url("disable"), json=data)

    async def generate_update_subscription_link(self, *, code):
        """
        Generate a link for updating the card on a subscription
        :param code: Subscription code
        :return: Response
        """
        return await self.get(url=self.url(f"{code}/manage/link"))

    async def send_update_subscription_link(self, *, code):
        """
        Email a customer a link for updating the card on their subscription
        :param code: Subscription code
        :return: Response
        """
        return await self.post(url=self.url(f"{code}/manage/email"))
