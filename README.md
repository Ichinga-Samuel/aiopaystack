# aiopaystack

Asynchronous Python library for [Paystack](https://paystack.com/)

Add your paystack secret key as an environment variable using  PAY_STACK_SECRET_KEY

```python
from aiopaystack.transactions import Transactions

trans = Transaction()

await trans.initialize(email="sam@gmail.com", amount='5000')
# All parameters must be passed in as keywords. For both required and optional arguments.

# passing secret key as an argument
# the paystack class is a singleton class and this will override any secret key placed as an environment variable
from aiopaystack.paystack import Paystack
paystack = Paystack(secret_key="paystack_secret_key")

# to use one session for multiple request use the class as a context manager

async with Transactions() as trans:
    await trans.verify(reference="ref")

## DOC Reference: <https://developers.paystack.co/v2.0/reference>
### Static Use
```
Don't forget to get your API key from [Paystack](https://paystack.com/) and assign to the variable `PAYSTACK_SECRET_KEY`
Please reference the **docs** folder for usage,
