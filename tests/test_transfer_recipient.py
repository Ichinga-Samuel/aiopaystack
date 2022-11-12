from paystack import TransferRecipient

from . import BaseTest, recipient, recipients


class TestTransferRecipient(BaseTest):
    async def tests(self, recipient, recipients):
        async with TransferRecipient() as tr:
            res = await tr.create(**recipient)
            assert res['message'] != ""

            res = await tr.bulk_create(**recipients)
            assert res['message'] != ""

            res = await tr.list()
            assert res['status'] is True

            res = await tr.fetch(id_or_code="djldlds")
            assert res['message'] != ""

            res = await tr.update(id_or_code='djldlds', name="Obi Datti")
            assert res['message'] != ""

            res = await tr.delete_transfer_recipient(id_or_code="djldlds")
            assert res['message'] != ""
