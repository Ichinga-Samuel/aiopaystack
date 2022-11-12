from paystack import Miscellaneous

from . import BaseTest


class TestMisc(BaseTest):

    async def tests(self):
        async with Miscellaneous() as misc:
            res = await misc.list_banks()
            assert res['status'] is True

            res = await misc.list_countries()
            print(res)
            assert res['status'] is True
            assert res['message'] != ""

            res = await misc.list_providers()
            assert res['status'] is True

            res = await misc.list_states(country="CA")
            assert res['status'] is True
