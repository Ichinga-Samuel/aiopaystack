from paystack import Customers
from . import BaseTest, customer, validate_customer


class TestCustomers(BaseTest):
    async def tests(self, customer, validate_customer):
        async with Customers() as customers:
            res = await customers.create(**customer)
            data = res['data']
            assert res['status'] is True

            res = await customers.list()
            assert res['status'] is True

            res = await customers.validate(code=data['customer_code'], value=data['id'], **validate_customer)
            assert res['status'] is True

            res = await customers.update(code=data['customer_code'], first_name="Ichinga", last_name="Samuel")
            assert res['message'] != ""

            res = await customers.fetch(email_or_code=data['customer_code'])
            assert res['status'] is True

            res = await customers.set_risk_action(customer=data['customer_code'], email=data['email'], risk_action='allow')
            assert res['status'] is True
