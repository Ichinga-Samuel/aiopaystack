from paystack import Plans

from . import BaseTest


class TestPlans(BaseTest):

    async def tests(self):
        async with Plans() as plans:
            res = await plans.create(name="Monthly retainer", interval="monthly", amount=500000)
            code = res['data']['id']
            assert res['status'] is True

            res = await plans.list()
            assert res['status'] is True

            res = await plans.fetch(id_or_code=code)
            assert res['status'] is True

            res = await plans.update(id_or_code=code, name="Monthly retainer", interval="monthly", amount=500000)
            assert res['status'] is True
