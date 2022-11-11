from paystack import TransferRecipient

from . import BaseTest


class TestTransferRecipient(BaseTest):
    rec = {"type": "nuban", "name": "Tolu Robert", "account_number": "0100000001", "bank_code": "063", "currency": "NGN"}
    batch = {"batch": [
        {
            "type": "nuban",
            "name": "Habenero Mundane",
            "account_number": "0123456789",
            "bank_code": "033",
            "currency": "NGN"
        },
        {
            "type": "nuban",
            "name": "Soft Merry",
            "account_number": "9876543231",
            "bank_code": "50211",
            "currency": "NGN"
        }]
    }

    async def test(self):
        async with TransferRecipient() as tr:
            res = await tr.create(**self.rec)
            assert res['message'] != ""

            res = await tr.bulk_create(**self.batch)
            assert res['message'] != ""

            res = await tr.list()
            assert res['status'] is True

            res = await tr.fetch(id_or_code="djldlds")
            assert res['message'] != ""

            res = await tr.update(id_or_code='djldlds', name="Obi Datti")
            assert res['message'] != ""

            res = await tr.delete_transfer_recipient(id_or_code="djldlds")
            assert res['message'] != ""
