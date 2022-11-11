from typing import Literal

from .base import Base


class TransferControl(Base):
    """
    The Transfers Control API allows you manage settings of your transfers
    """
    def __init__(self):
        super().__init__()
        url = "/{}"
        self.url = url.format

    async def check_balance(self):
        """
        Fetch the available balance on your integration
        :return: Response
        """
        return await self.get(url=self.url("balance"))

    async def fetch_balance_ledger(self):
        """
        Fetch all pay-ins and pay-outs that occured on your integration
        :return: Response
        """
        return await self.get(url=self.url("balance/ledger"))

    async def resend_transfer_otp(self, *, transfer_code: str, reason: Literal['resend_otp', 'transfer']):
        """
        Generates a new OTP and sends to customer in the event they are having trouble receiving one.
        :param transfer_code: Transfer code
        :param reason: Either resend_otp or transfer
        :return: Response
        """
        data = {'transfer_code': transfer_code, 'reason': reason}
        return await self.post(url=self.url(""), json=data)

    async def disable_transfers_otp(self):
        """
        This is used in the event that you want to be able to complete transfers programmatically without use of OTPs. No arguments required.
         You will get an OTP to complete the request.
        :return: Response
        """
        return await self.post(url=self.url("transfer/disable_otp"))

    async def finalize_disable_otp(self, *, otp: str):
        """
        Finalize the request to disable OTP on your transfers.
        :param otp: OTP sent to business phone to verify disabling OTP requirement
        :return: Response
        """
        data = {'otp': otp}
        return await self.post(url=self.url("transfer/disable_otp_finalize"), json=data)

    async def enable_transfers_otp(self):
        """
        In the event that a customer wants to stop being able to complete transfers programmatically, this endpoint helps turn
        OTP requirement back on. No arguments required.
        :return: Response
        """
        return await self.post(url=self.url("transfer/enable_otp"))
