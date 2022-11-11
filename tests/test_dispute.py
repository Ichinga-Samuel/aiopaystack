from paystack import Disputes
from . import BaseTest


class TestDisputes(BaseTest):
    async def test_dispute(self):
        async with Disputes() as disputes:
            res = await disputes.list(from_="2022-11-01", to="2022-11-10")
            assert res['status'] is True

            res = await disputes.fetch(id='1234')
            assert res['message'] != ""

            res = await disputes.list_transaction_disputes(id='1234')
            assert res['message'] != ""

            res = await disputes.update(id='1234', refund_amount=50000)
            assert res['message'] != ""

            res = await disputes.add_evidence(id='1234', customer_name="Sam", customer_email="sam@gmail.com", customer_phone="+2349037031782",
                                              service_details="not ok")
            assert res['message'] != ""

            res = await disputes.get_upload_url(id='1234', upload_filename="test_dispute.py")
            data = res['data']
            assert res['status'] is True

            res = await disputes.resolve(id="1234", resolution="declined", uploaded_filename=data['fileName'], message="Unresolved", refund_amount=5000)
            assert res['message'] != ""

            res = await disputes.export(from_="2022-11-01", to="2022-11-10")
            assert res['message'] != ""

