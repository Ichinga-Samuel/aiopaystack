<a id="paystack.transactions"></a>

# paystack.transactions

<a id="paystack.transactions.Transactions"></a>

## Transactions Objects

```python
class Transactions(Base)
```

The Transactions API allows you create and manage payments on your integration

<a id="paystack.transactions.Transactions.initialize"></a>

#### initialize

```python
async def initialize(*, email: str, amount: str, **kwargs)
```

Initialize transaction. Email and amount are required fields

**Arguments**:

- `amount`: Amount should be in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR
- `email`: Customer's email address
- `kwargs`: optional params of request body as keyword arguments

**Returns**:

json data from paystack API as a dict

<a id="paystack.transactions.Transactions.verify"></a>

#### verify

```python
async def verify(*, reference: str)
```

**Arguments**:

- `reference`: The transaction reference used to initiate the transaction

**Returns**:

json data from paystack API

<a id="paystack.transactions.Transactions.list"></a>

#### list

```python
async def list(*,
               perPage: int = 50,
               page: int = 1,
               from_: datetime | None = None,
               **kwargs)
```

List transactions carried out on your integration.

**Arguments**:

- `page`: Specify exactly what page you want to retrieve. If not specify we use a default value of 1.
- `perPage`: Specify how many records you want to retrieve per page. If not specify we use a default value of 50.
- `from_`: from should be added this way
- `kwargs`: Optional query parameters as keyword arguments

**Returns**:

List of transactions as json data from paystack API

<a id="paystack.transactions.Transactions.fetch"></a>

#### fetch

```python
async def fetch(*, id)
```

Get details of a transaction carried out on your integration.

**Arguments**:

- `id`: id of a single transaction

**Returns**:

json data from paystack API

<a id="paystack.transactions.Transactions.charge_authorization"></a>

#### charge\_authorization

```python
async def charge_authorization(*, amount: str, email: str,
                               authorization_code: str, **kwargs)
```

All authorizations marked as reusable can be charged with this endpoint whenever you need to receive payments.

**Arguments**:

- `authorization_code`: Valid authorization code to charge
- `email`: Customer's email address
- `amount`: Amount should be in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR
- `kwargs`: optional params of request body as keyword arguments

**Returns**:

json data from paystack API

<a id="paystack.transactions.Transactions.check_authorization"></a>

#### check\_authorization

```python
async def check_authorization(*, amount: str, email: str,
                              authorization_code: str, **kwargs)
```

All Mastercard and Visa authorizations can be checked with this endpoint to know if they have

funds for the payment you seek. This endpoint should be used when you do not know the exact amount to
charge a card when rendering a service. It should be used to check if a card has enough funds based on
a maximum range value. It is well suited for:
Ride hailing services
Logistics services

**Arguments**:

- `authorization_code`: Valid authorization code to charge
- `email`: Customer's email address
- `amount`: Amount should be in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR
- `kwargs`: optional params of request body as keyword arguments

**Returns**:

json data from paystack API

<a id="paystack.transactions.Transactions.view_transaction_timeline"></a>

#### view\_transaction\_timeline

```python
async def view_transaction_timeline(*, id_or_reference: str)
```

View the timeline of a transaction

**Arguments**:

- `id_or_reference`: id or reference of transaction

**Returns**:

json data from paystack API

<a id="paystack.transactions.Transactions.transaction_totals"></a>

#### transaction\_totals

```python
async def transaction_totals(*,
                             perPage: int = 50,
                             page: int = 1,
                             from_: datetime | None = None,
                             to: datetime | None = None)
```

If you specify a page number also specify a results per page. eg page=1, perPage=10

You can specify from and to as query parameters

**Arguments**:

- `page`: Specify exactly what page you want to retrieve. If not specify we use a default value of 1.
- `perPage`: Specify how many records you want to retrieve per page. If not specify we use a default value of 50.
- `to`: Specify exactly what page you want to retrieve. If not specify we use a default value of 1.
- `from_`: A timestamp from which to start listing transaction e.g. 2016-09-24T00:00:05.000Z, 2016-09-21

**Returns**:

Response

<a id="paystack.transactions.Transactions.export_transactions"></a>

#### export\_transactions

```python
async def export_transactions(perPage: int = 50, page: int = 1, **kwargs)
```

If you specify a page number also specify a results per page. eg page=1, perPage=10

**Arguments**:

- `perPage`: Specify how many records you want to retrieve per page. If not specify we use a default value of 50.
- `page`: Specify exactly what page you want to retrieve. If not specify we use a default value of 1.
- `kwargs`: 

**Returns**:

Response

<a id="paystack.transactions.Transactions.partial_debit"></a>

#### partial\_debit

```python
async def partial_debit(*, authorization_code: str, email: str, amount: str,
                        currency: Literal['NGN', 'GHS', 'ZAR',
                                          'USD'], **kwargs)
```

Retrieve part of a payment from a customer

authorization_code, currency, amount, email are required fields

**Arguments**:

- `authorization_code`: Valid authorization code to charge
- `email`: Customer's email address
- `amount`: Amount should be in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR
- `currency`: Specify the currency you want to debit. Allowed values are NGN, GHS, ZAR or USD.
- `kwargs`: keyword arguments form body of requests

**Returns**:

Response

