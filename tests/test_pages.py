from paystack import PaymentPages

from . import BaseTest


class TestPaymentPages(BaseTest):

    async def tests(self):
        async with PaymentPages() as pp:
            res = await pp.create(name="GOTV")
            data = res['data']
            assert res['status'] is True

            res = await pp.list()
            assert res['status'] is True

            res = await pp.fetch(id_or_slug=data["id"])
            assert res['status'] is True

            res = await pp.update(id_or_slug=data['id'], name="GOTV", description="GOTV Max")
            assert res['status'] is True

            res = await pp.is_slug_available(slug="slug")
            assert res['status'] is True

            res = await pp.add_products(id=data['id'], product=[244, 5665])
            assert res['message'] != ""
