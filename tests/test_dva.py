from paystack import DedicatedVirtualAccount
from . import BaseTest, dvac, customer, customers


class TestDedicatedVirtualAccount(BaseTest):

    async def tests(self, dvac):
        async with DedicatedVirtualAccount() as dva:
            res = await dva.create(customer="CUS_hpu6h031764sunl", preferred_bank="wema-bank")
            assert res['status'] is True

            # res = await dva.assign(**get_dva)
            # assert res['message'] != ""
            #
            # res = await dva.list(active=False)
            # assert res['message'] != ""
            #
            # res = await dva.fetch(dedicated_account_id='dedid')
            # assert res['message'] != ""
            #
            # res = await dva.deactivate(dedicated_account_id='dedid')
            # assert res['message'] != ""
            #
            # res = await dva.split(customer="Cusdkjdjkjks")
            # assert res['message'] != ""
            #
            # res = await dva.requery(account_number="1234567890", provider_slug="wema-bank")
            # assert res['message'] != ""
            #
            # res = await dva.remove_split(account_number="1234567890")
            # assert res['message'] != ""
            #
            # res = await dva.fetch_providers()
            # assert res['message'] != ""
