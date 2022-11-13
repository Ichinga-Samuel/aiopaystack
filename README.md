# aiopaystack

Asynchronous Python library for [Paystack](https://paystack.com/)

## Installation
```bash
pip install aiopaystack
```

## Usage
Add your paystack secret key as an environment variable as PAY_STACK_SECRET_KEY
```python
from paystack import Transactions

trans = Transactions()

# All parameters must be passed in as keywords. For both required and optional arguments.
res = await trans.initialize(email="sam@gmail.com", amount='5000')

# Passing secret key as an argument
# This replaces any key set in the environment
from paystack import Paystack
paystack = Paystack(secret_key="paystack_secret_key")

# to use one session for multiple request use the class as a context manager
async with Transactions() as trans:
    res= await trans.verify(reference="ref")
    
# The response type for every request is a typed dict.
from typing import TypedDict, Any
Response = TypedDict('Response', {'status_code': int, 'status': bool, 'message': str, 'data': dict | Any})

# Sample response
{'status': True,
 'message': 'Authorization URL created',
 'data': 
     {'authorization_url': 'https://checkout.paystack.com/3521i62zf1i0ljl',
      'access_code': '3521i62zf1i0ljl', 'reference': '2q16btxglw'
      },
 'status_code': 200
 }
## DOC Reference: <https://developers.paystack.co/v2.0/reference>
### Static Use
```
Don't forget to get your API key from [Paystack](https://paystack.com/) and assign to the variable `PAYSTACK_SECRET_KEY`
Please reference the **docs** folder for usage,
