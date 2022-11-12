from datetime import date
from . import BaseTest
from .fixtures import init_charge
from paystack import Charge


class TestCharge(BaseTest):
    async def tests(self, init_charge):
        async with Charge() as charge:
            res = await charge.create(**init_charge)
            data = res['data']
            assert res['message'] != ""

            res = await charge.submit_pin(pin="5467", reference=data['reference'])
            assert res['message'] != ""

            res = await charge.submit_otp(otp="123467", reference=data['reference'])
            assert res['message'] != ""

            res = await charge.submit_phone(phone="0801234567", reference=data['reference'])
            assert res['message'] != ""

            res = await charge.submit_birthday(birthday="1990-1-31)", reference=data['reference'])
            assert res['message'] != ""

            res = await charge.submit_address(address="10 Wall Street", city="Benin", state="Edo", zipcode="654321",
                                              reference=data['reference'])
            assert res['message'] != ""

            res = await charge.check_pending(reference=data['reference'])
            assert res['status'] is True
