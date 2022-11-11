from paystack import BulkCharge

from . import BaseTest, charges


class TestBulkCharge(BaseTest):
    async def test_bulk(self, charges):
        async with BulkCharge() as bulk_charge:
            res = await bulk_charge.initiate(charges=charges)
            data = res['data']
            assert res['status'] is True

            res = await bulk_charge.list()
            assert res['status'] is True

            res = await bulk_charge.fetch_bulk_charge_batch(id_or_code=data['batch_code'])
            assert res['status'] is True

            res = await bulk_charge.fetch_charges_in_a_batch(id_or_code=data['batch_code'])
            assert res['status'] is True

            res = await bulk_charge.pause_bulk_charge(batch_code=data['batch_code'])
            assert res['status'] is True

            res = await bulk_charge.resume_bulk_charge(batch_code=data['batch_code'])
            assert res['status'] is True
