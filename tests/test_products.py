from paystack import Products
from . import BaseTest


class TestProducts(BaseTest):
    async def tests(self):
        async with Products() as products:
            res = await products.create(name="The Product", description="An Awesome Product", price=500000, currency="NGN")
            data = res['data']
            assert res['status'] is True

            res = await products.list()
            assert res['status'] is True

            res = await products.fetch(id=data['id'])
            assert res['status'] is True

            res = await products.update(id=data['id'], name="A Product", description="Still Awesome at 600000", price=600000, currency="NGN")
            assert res['status'] is True
