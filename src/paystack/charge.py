from datetime import date

from .base import Base


class Charge(Base):
    """
    The Charge API allows you to configure payment channel of your choice when initiating a payment.
    """

    def __init__(self):
        super().__init__()
        url = "/charge/"
        self.url = url.format

    async def create(self, *, email: str, amount: str, **kwargs):
        """
        Initiate a payment by integrating the payment channel of your choice.
        :param email: Customer's email address
        :param amount: Amount should be in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR
        :param kwargs:
        :return: Response
        """

        data = {'email': email, 'amount': amount, **kwargs}
        return await self.post(url=self.url(""), json=data)

    async def submit_pin(self, *, pin: str, reference: str):
        """
        Submit PIN to continue a charge
        :param pin: PIN submitted by user
        :param reference: Reference for transaction that requested pin
        :return: Response
        """
        data = {'pin': pin, 'reference': reference}
        return await self.post(url=self.url("submit_pin"), json=data)

    async def submit_otp(self, *, otp: str, reference: str):
        """
        Submit OTP to complete a charge
        :param otp: OTP submitted by user
        :param reference: Reference for ongoing transaction
        :return: Response
        """
        data = {'otp': otp, 'reference': reference}
        return await self.post(url=self.url("submit_otp"), json=data)

    async def submit_phone(self, *, phone: str, reference: str):
        """
        Submit Phone when requested
        :param phone: Phone submitted by user
        :param reference: Reference for ongoing transaction
        :return: Response
        """
        data = {'phone': phone, 'reference': reference}
        return await self.post(url=self.url("submit_phone"), json=data)

    async def submit_birthday(self, *, birthday: date, reference: str):
        """
        Submit Birthday when requested
        :param birthday: Birthday submitted by user e.g. 2016-09-21
        :param reference: Reference for ongoing transaction
        :return: Response
        """
        data = {'birthday': birthday, 'reference': reference}
        return await self.post(url=self.url("submit_birthday"), json=data)

    async def submit_address(self, *, address: str, reference: str, city: str, state: str, zipcode: str):
        """
        Submit address to continue a charge
        :param address: Address submitted by user
        :param reference: Reference for ongoing transaction
        :param city: City submitted by user
        :param state: State submitted by user
        :param zipcode: Zipcode submitted by user
        :return: Response
        """
        data = {'address': address, 'reference': reference, 'city': city, 'state': state, 'zipcode': zipcode}
        return await self.post(url=self.url("submit_address"), json=data)

    async def check_pending(self, *, reference: str):
        """
        Check Pending Charge
        :param reference: The reference to check
        :return: Response
        """
        params = {'reference': reference}
        return await self.get(url=self.url(f"{reference}"), params=params)
