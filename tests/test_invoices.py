from paystack import Invoices

from . import BaseTest, invoice


class TestInvoices(BaseTest):

    async def tests(self, invoice):
        async with Invoices() as invoices:
            res = await invoices.create(**invoice)
            assert res['message'] != ""

            res = await invoices.list(customer="CUs fdf", status="true", currency="NGN", include_archive='yes')
            assert res['status'] is True

            res = await invoices.view(id_or_code="934304")
            assert res['message'] != ""

            res = await invoices.verify(code="934304")
            assert res['status'] is True

            res = await invoices.send_notification(code="934304")
            assert res['message'] != ""

            res = await invoices.invoice_totals()
            assert res['status'] is True

            res = await invoices.finalize_invoice(code="934304")
            assert res['message'] != ""

            res = await invoices.update(id_or_code="934304", customer="Cudlne")
            assert res['data'] == {}

            res = await invoices.archive(id_or_code="934304")
            assert res['message'] != ""
