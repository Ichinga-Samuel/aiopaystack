from paystack.control_panel import ControlPanel

from . import BaseTest


class TestControlPanel(BaseTest):
    cp = ControlPanel()

    async def tests(self):
        async with self.cp as cp:
            res = await cp.fetch_payment_session_timeout()
            assert res['status'] is True

            res = await cp.update_payment_session_timeout(timeout=2)
            assert res['status'] is True
