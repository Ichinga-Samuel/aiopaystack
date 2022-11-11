from paystack import TransferControl

from . import BaseTest


class TestTransferControl(BaseTest):
    async def test(self):
        async with TransferControl() as transfer_control:
            res = await transfer_control.check_balance()
            assert res['status'] is True

            res = await transfer_control.fetch_balance_ledger()
            assert res['status'] is True

            res = await transfer_control.disable_transfers_otp()
            assert res['status'] is True

            res = await transfer_control.enable_transfers_otp()
            assert res['status'] is True

            res = await transfer_control.finalize_disable_otp(otp="123456")
            assert res['message'] != ""

            res = await transfer_control.resend_transfer_otp(transfer_code="TRF_vsyqdmlzble3uii", reason="transfer")
            assert res['message'] != ""
