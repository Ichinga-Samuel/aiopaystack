from paystack import Customers
from . import BaseTest, customer, customers
from random import choice, randint


class TestCustomers(BaseTest):
    async def tests(self, customer, customers):
        async with Customers() as cus:
            # Test customer creation
            res = await cus.create(**customer)
            data = res['data']
            assert data['email'] == customer['email']
            customer |= data

            # Test customers listing
            res = await cus.list(perPage=50)
            data = res['data']
            customers.extend(data)
            assert res['status'] is True

            # Test customer fetching
            res = await cus.fetch(email_or_code=customer['customer_code'])
            data = res['data']
            assert data['customer_code'] == customer['customer_code']

            # Test customer updating
            c = choice(customers)
            res = await cus.update(code=c['customer_code'], metadata={'available': True})
            data = res['data']
            assert data['metadata']['available'] is True

            # Test customer validation
            customer['account_number'] = str(randint(1000000000, 9999999999))
            res = await cus.validate(code=customer['customer_code'], **customer)
            assert res['status'] is True

            # Test customer blacklisting
            res = await cus.set_risk_action(customer=customer['customer_code'], email=customer['email'], risk_action='deny')
            assert res['status'] is True
