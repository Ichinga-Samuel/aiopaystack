from paystack import Transfers

from . import BaseTest, initiate_transfer, bulk_transfer


class TestTransfers(BaseTest):

    async def tests(self, initiate_transfer, bulk_transfer):
        async with Transfers() as transfers:
            res = await transfers.initiate(**initiate_transfer)
            assert res['message'] != ""

            res = await transfers.finalize(transfer_code="TRF_vsyqdmlzble3uii", otp="928783")
            assert res['message'] != ""

            res = await transfers.initiate_bulk_transfer(**bulk_transfer)
            assert res['message'] != ""

            res = await transfers.list(customer="dgbdfgkear")
            assert res['status'] is True

            res = await transfers.fetch(id_or_code="TRF_2x5j67tnnw1t98k")
            assert res['status'] is True

            res = await transfers.verify(reference="ref_demo")
            assert res['status'] is True
