from .base import Base


class ControlPanel(Base):
    """
    The Control Panel API allows you manage some settings on your integration
    """
    def __init__(self):
        super().__init__()
        url = "/integration/{}"
        self.url = url.format

    async def fetch_payment_session_timeout(self):
        """
        Fetch the payment session timeout on your integration
        :return: Response
        """
        return await self.get(url=self.url("payment_session_timeout"))

    async def update_payment_session_timeout(self, *, timeout: int):
        """
        Update the payment session timeout on your integration
        :param timeout: Time before stopping session (in seconds). Set to 0 to cancel session timeouts
        :return: Response
        """
        data = {'timeout': timeout}
        return await self.put(url=self.url("payment_session_timeout"), json=data)
