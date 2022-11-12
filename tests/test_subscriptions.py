from paystack import Subscriptions

from . import BaseTest


class TestSubscriptions(BaseTest):

    async def tests(self):
        async with Subscriptions() as subs:
            res = await subs.create(customer="customer@email.com", plan="PLN_gx2wn530m0i3w3m")
            assert res['message'] != ""

            res = await subs.list()
            assert res['status'] is True

            res = await subs.fetch(id_or_code="sub_id")
            assert res['status'] is True

            res = await subs.enable(code="SUB_vsyqdmlzble3uii", token="d7gofp6yppn3qz7")
            assert res['message'] != ""

            res = await subs.disable(code="SUB_vsyqdmlzble3uii", token="d7gofp6yppn3qz7")
            assert res['message'] != ""

            res = await subs.generate_update_subscription_link(code="sub_id")
            assert res['status'] is True

            res = await subs.send_update_subscription_link(code="sub_id")
            assert res['message'] != ""
