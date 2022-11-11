from datetime import date
from . import BaseTest
from .fixtures import init_charge
from paystack import Charge


class TestCharge(BaseTest):
    async def test_charge(self, init_charge):
        async with Charge() as charge:
            res = await charge.create(**init_charge)
            data = res['data']
            assert res['status'] is True

            res = await charge.submit_pin(pin="5467", reference=data['reference'])
            assert res['status'] is True

            res = await charge.submit_otp(otp="123467", reference=data['reference'])
            assert res['status'] is True

            res = await charge.submit_phone(phone="09037031782", reference=data['reference'])
            assert res['status'] is True

            res = await charge.submit_birthday(birthday="1995-11-18)", reference=data['reference'])
            assert res['status'] is True

            res = await charge.submit_address(address="13 Uzuakoli Street", city="Port Harcourt", state="Rivers", zipcode="502103",
                                              reference=data['reference'])
            assert res['status'] is True

            res = await charge.check_pending(reference=data['reference'])
            assert res['status'] is True
