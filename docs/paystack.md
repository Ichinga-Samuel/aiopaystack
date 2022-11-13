# Table of Contents

* [paystack](#paystack)
* [paystack.apple\_pay](#paystack.apple_pay)
  * [ApplePay](#paystack.apple_pay.ApplePay)
    * [register](#paystack.apple_pay.ApplePay.register)
    * [list](#paystack.apple_pay.ApplePay.list)
    * [unregister](#paystack.apple_pay.ApplePay.unregister)
* [paystack.base](#paystack.base)
* [paystack.bulkcharge](#paystack.bulkcharge)
  * [BulkCharge](#paystack.bulkcharge.BulkCharge)
    * [initiate](#paystack.bulkcharge.BulkCharge.initiate)
    * [list](#paystack.bulkcharge.BulkCharge.list)
    * [fetch\_bulk\_charge\_batch](#paystack.bulkcharge.BulkCharge.fetch_bulk_charge_batch)
    * [fetch\_charges\_in\_a\_batch](#paystack.bulkcharge.BulkCharge.fetch_charges_in_a_batch)
    * [pause\_bulk\_charge](#paystack.bulkcharge.BulkCharge.pause_bulk_charge)
    * [resume\_bulk\_charge](#paystack.bulkcharge.BulkCharge.resume_bulk_charge)
* [paystack.charge](#paystack.charge)
  * [Charge](#paystack.charge.Charge)
    * [create](#paystack.charge.Charge.create)
    * [submit\_pin](#paystack.charge.Charge.submit_pin)
    * [submit\_otp](#paystack.charge.Charge.submit_otp)
    * [submit\_phone](#paystack.charge.Charge.submit_phone)
    * [submit\_birthday](#paystack.charge.Charge.submit_birthday)
    * [submit\_address](#paystack.charge.Charge.submit_address)
    * [check\_pending](#paystack.charge.Charge.check_pending)
* [paystack.control\_panel](#paystack.control_panel)
  * [ControlPanel](#paystack.control_panel.ControlPanel)
    * [fetch\_payment\_session\_timeout](#paystack.control_panel.ControlPanel.fetch_payment_session_timeout)
    * [update\_payment\_session\_timeout](#paystack.control_panel.ControlPanel.update_payment_session_timeout)
* [paystack.customers](#paystack.customers)
  * [Customers](#paystack.customers.Customers)
    * [create](#paystack.customers.Customers.create)
    * [list](#paystack.customers.Customers.list)
    * [fetch](#paystack.customers.Customers.fetch)
    * [update](#paystack.customers.Customers.update)
    * [validate](#paystack.customers.Customers.validate)
    * [set\_risk\_action](#paystack.customers.Customers.set_risk_action)
    * [deactivate\_authorization](#paystack.customers.Customers.deactivate_authorization)
* [paystack.dedicated\_virtual\_accounts](#paystack.dedicated_virtual_accounts)
  * [DedicatedVirtualAccount](#paystack.dedicated_virtual_accounts.DedicatedVirtualAccount)
    * [create](#paystack.dedicated_virtual_accounts.DedicatedVirtualAccount.create)
    * [assign](#paystack.dedicated_virtual_accounts.DedicatedVirtualAccount.assign)
    * [list](#paystack.dedicated_virtual_accounts.DedicatedVirtualAccount.list)
    * [fetch](#paystack.dedicated_virtual_accounts.DedicatedVirtualAccount.fetch)
    * [deactivate](#paystack.dedicated_virtual_accounts.DedicatedVirtualAccount.deactivate)
    * [split](#paystack.dedicated_virtual_accounts.DedicatedVirtualAccount.split)
    * [requery](#paystack.dedicated_virtual_accounts.DedicatedVirtualAccount.requery)
    * [remove\_split](#paystack.dedicated_virtual_accounts.DedicatedVirtualAccount.remove_split)
    * [fetch\_providers](#paystack.dedicated_virtual_accounts.DedicatedVirtualAccount.fetch_providers)
* [paystack.disputes](#paystack.disputes)
  * [Disputes](#paystack.disputes.Disputes)
    * [list](#paystack.disputes.Disputes.list)
    * [fetch](#paystack.disputes.Disputes.fetch)
    * [list\_transaction\_disputes](#paystack.disputes.Disputes.list_transaction_disputes)
    * [update](#paystack.disputes.Disputes.update)
    * [add\_evidence](#paystack.disputes.Disputes.add_evidence)
    * [get\_upload\_url](#paystack.disputes.Disputes.get_upload_url)
    * [resolve](#paystack.disputes.Disputes.resolve)
    * [export](#paystack.disputes.Disputes.export)
* [paystack.invoices](#paystack.invoices)
  * [Invoices](#paystack.invoices.Invoices)
    * [create](#paystack.invoices.Invoices.create)
    * [list](#paystack.invoices.Invoices.list)
    * [view](#paystack.invoices.Invoices.view)
    * [verify](#paystack.invoices.Invoices.verify)
    * [send\_notification](#paystack.invoices.Invoices.send_notification)
    * [invoice\_totals](#paystack.invoices.Invoices.invoice_totals)
    * [finalize\_invoice](#paystack.invoices.Invoices.finalize_invoice)
    * [update](#paystack.invoices.Invoices.update)
    * [archive](#paystack.invoices.Invoices.archive)
* [paystack.misc](#paystack.misc)
  * [Miscellaneous](#paystack.misc.Miscellaneous)
    * [list\_banks](#paystack.misc.Miscellaneous.list_banks)
    * [list\_providers](#paystack.misc.Miscellaneous.list_providers)
    * [list\_countries](#paystack.misc.Miscellaneous.list_countries)
    * [list\_states](#paystack.misc.Miscellaneous.list_states)
* [paystack.page](#paystack.page)
  * [PaymentPages](#paystack.page.PaymentPages)
    * [create](#paystack.page.PaymentPages.create)
    * [list](#paystack.page.PaymentPages.list)
    * [fetch](#paystack.page.PaymentPages.fetch)
    * [update](#paystack.page.PaymentPages.update)
    * [is\_slug\_available](#paystack.page.PaymentPages.is_slug_available)
    * [add\_products](#paystack.page.PaymentPages.add_products)
* [paystack.paystack](#paystack.paystack)
* [paystack.plans](#paystack.plans)
  * [Plans](#paystack.plans.Plans)
    * [create](#paystack.plans.Plans.create)
    * [list](#paystack.plans.Plans.list)
    * [fetch](#paystack.plans.Plans.fetch)
    * [update](#paystack.plans.Plans.update)
* [paystack.products](#paystack.products)
  * [Products](#paystack.products.Products)
    * [create](#paystack.products.Products.create)
    * [list](#paystack.products.Products.list)
    * [fetch](#paystack.products.Products.fetch)
    * [update](#paystack.products.Products.update)
* [paystack.refund](#paystack.refund)
  * [Refund](#paystack.refund.Refund)
    * [create](#paystack.refund.Refund.create)
    * [list](#paystack.refund.Refund.list)
    * [fetch](#paystack.refund.Refund.fetch)
* [paystack.settlements](#paystack.settlements)
  * [Settlements](#paystack.settlements.Settlements)
    * [fetch](#paystack.settlements.Settlements.fetch)
    * [fetch\_settlement\_transactions](#paystack.settlements.Settlements.fetch_settlement_transactions)
* [paystack.subaccounts](#paystack.subaccounts)
  * [SubAccounts](#paystack.subaccounts.SubAccounts)
    * [create](#paystack.subaccounts.SubAccounts.create)
    * [list](#paystack.subaccounts.SubAccounts.list)
    * [fetch](#paystack.subaccounts.SubAccounts.fetch)
    * [update](#paystack.subaccounts.SubAccounts.update)
* [paystack.subscriptions](#paystack.subscriptions)
  * [Subscriptions](#paystack.subscriptions.Subscriptions)
    * [create](#paystack.subscriptions.Subscriptions.create)
    * [list](#paystack.subscriptions.Subscriptions.list)
    * [fetch](#paystack.subscriptions.Subscriptions.fetch)
    * [enable](#paystack.subscriptions.Subscriptions.enable)
    * [disable](#paystack.subscriptions.Subscriptions.disable)
    * [generate\_update\_subscription\_link](#paystack.subscriptions.Subscriptions.generate_update_subscription_link)
    * [send\_update\_subscription\_link](#paystack.subscriptions.Subscriptions.send_update_subscription_link)
* [paystack.transactions](#paystack.transactions)
  * [Transactions](#paystack.transactions.Transactions)
    * [initialize](#paystack.transactions.Transactions.initialize)
    * [verify](#paystack.transactions.Transactions.verify)
    * [list](#paystack.transactions.Transactions.list)
    * [fetch](#paystack.transactions.Transactions.fetch)
    * [charge\_authorization](#paystack.transactions.Transactions.charge_authorization)
    * [check\_authorization](#paystack.transactions.Transactions.check_authorization)
    * [view\_transaction\_timeline](#paystack.transactions.Transactions.view_transaction_timeline)
    * [transaction\_totals](#paystack.transactions.Transactions.transaction_totals)
    * [export\_transactions](#paystack.transactions.Transactions.export_transactions)
    * [partial\_debit](#paystack.transactions.Transactions.partial_debit)
* [paystack.transaction\_splits](#paystack.transaction_splits)
  * [TransactionSplits](#paystack.transaction_splits.TransactionSplits)
    * [create](#paystack.transaction_splits.TransactionSplits.create)
    * [list](#paystack.transaction_splits.TransactionSplits.list)
    * [search](#paystack.transaction_splits.TransactionSplits.search)
    * [fetch](#paystack.transaction_splits.TransactionSplits.fetch)
    * [update](#paystack.transaction_splits.TransactionSplits.update)
    * [add\_split\_subaccount](#paystack.transaction_splits.TransactionSplits.add_split_subaccount)
    * [remove\_subaccount\_from\_split](#paystack.transaction_splits.TransactionSplits.remove_subaccount_from_split)
* [paystack.transfers](#paystack.transfers)
  * [Transfers](#paystack.transfers.Transfers)
    * [initiate](#paystack.transfers.Transfers.initiate)
    * [finalize](#paystack.transfers.Transfers.finalize)
    * [initiate\_bulk\_transfer](#paystack.transfers.Transfers.initiate_bulk_transfer)
    * [list](#paystack.transfers.Transfers.list)
    * [fetch](#paystack.transfers.Transfers.fetch)
    * [verify](#paystack.transfers.Transfers.verify)
* [paystack.transfer\_control](#paystack.transfer_control)
  * [TransferControl](#paystack.transfer_control.TransferControl)
    * [check\_balance](#paystack.transfer_control.TransferControl.check_balance)
    * [fetch\_balance\_ledger](#paystack.transfer_control.TransferControl.fetch_balance_ledger)
    * [resend\_transfer\_otp](#paystack.transfer_control.TransferControl.resend_transfer_otp)
    * [disable\_transfers\_otp](#paystack.transfer_control.TransferControl.disable_transfers_otp)
    * [finalize\_disable\_otp](#paystack.transfer_control.TransferControl.finalize_disable_otp)
    * [enable\_transfers\_otp](#paystack.transfer_control.TransferControl.enable_transfers_otp)
* [paystack.transfer\_recipient](#paystack.transfer_recipient)
  * [TransferRecipient](#paystack.transfer_recipient.TransferRecipient)
    * [create](#paystack.transfer_recipient.TransferRecipient.create)
    * [bulk\_create](#paystack.transfer_recipient.TransferRecipient.bulk_create)
    * [list](#paystack.transfer_recipient.TransferRecipient.list)
    * [fetch](#paystack.transfer_recipient.TransferRecipient.fetch)
    * [update](#paystack.transfer_recipient.TransferRecipient.update)
    * [delete\_transfer\_recipient](#paystack.transfer_recipient.TransferRecipient.delete_transfer_recipient)
* [paystack.verification](#paystack.verification)
  * [Verification](#paystack.verification.Verification)
    * [resolve\_account\_number](#paystack.verification.Verification.resolve_account_number)
    * [validate\_account](#paystack.verification.Verification.validate_account)
    * [resolve\_card\_bin](#paystack.verification.Verification.resolve_card_bin)

<a id="paystack"></a>

# paystack

<a id="paystack.apple_pay"></a>

# paystack.apple\_pay

<a id="paystack.apple_pay.ApplePay"></a>

## ApplePay Objects

```python
class ApplePay(Base)
```

The Apple Pay API allows you register your application's top-level domain or subdomain

<a id="paystack.apple_pay.ApplePay.register"></a>

#### register

```python
async def register(domainName: str)
```

Register a top-level domain or subdomain for your Apple Pay integration.

**Arguments**:

- `domainName`: Domain name to be registered

**Returns**:

Response

<a id="paystack.apple_pay.ApplePay.list"></a>

#### list

```python
async def list()
```

Lists all registered domains on your integration. Returns an empty array if no domains have been added.

**Returns**:

Response

<a id="paystack.apple_pay.ApplePay.unregister"></a>

#### unregister

```python
async def unregister(domainName: str)
```

Unregister a top-level domain or subdomain previously used for your Apple Pay integration.

**Arguments**:

- `domainName`: Domain name to be registered

**Returns**:

Response

<a id="paystack.base"></a>

# paystack.base

<a id="paystack.bulkcharge"></a>

# paystack.bulkcharge

<a id="paystack.bulkcharge.BulkCharge"></a>

## BulkCharge Objects

```python
class BulkCharge(Base)
```

The Bulk Charges API allows you create and manage multiple recurring payments from your customers

<a id="paystack.bulkcharge.BulkCharge.initiate"></a>

#### initiate

```python
async def initiate(charges: list[dict])
```

Send an array of objects with authorization codes and amount (in kobo if currency is NGN, pesewas,

if currency is GHS, and cents, if currency is ZAR ) so we can process transactions as a batch.

**Arguments**:

- `charges`: A list of charge object. Each object consists of an authorization, amount and reference

**Returns**:

Response

<a id="paystack.bulkcharge.BulkCharge.list"></a>

#### list

```python
async def list(*,
               perPage: int = 50,
               page: int = 1,
               from_: datetime | None | str = None,
               to: datetime | None | str = None)
```

This lists all bulk charge batches created by the integration. Statuses can be active, paused, or complete.

**Arguments**:

- `perPage`: Specify how many records you want to retrieve per page. If not specify we use a default value of 50.
- `page`: Specify exactly what page you want to retrieve. If not specify we use a default value of 1.
- `from_`: A timestamp from which to start listing batches e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
- `to`: A timestamp at which to stop listing batches e.g. 2016-09-24T00:00:05.000Z, 2016-09-21

**Returns**:

Response

<a id="paystack.bulkcharge.BulkCharge.fetch_bulk_charge_batch"></a>

#### fetch\_bulk\_charge\_batch

```python
async def fetch_bulk_charge_batch(*, id_or_code: str)
```

This endpoint retrieves a specific batch code. It also returns useful information on its progress by way of the total_charges

and pending_charges attributes.

**Arguments**:

- `id_or_code`: An ID or code for the charge whose batches you want to retrieve.

**Returns**:

Response

<a id="paystack.bulkcharge.BulkCharge.fetch_charges_in_a_batch"></a>

#### fetch\_charges\_in\_a\_batch

```python
async def fetch_charges_in_a_batch(*,
                                   id_or_code: str,
                                   perPage: int = 50,
                                   page: int = 1,
                                   from_: datetime | None | str = None,
                                   to: datetime | None | str = None)
```

This endpoint retrieves the charges associated with a specified batch code. Pagination parameters are available.

You can also filter by status. Charge statuses can be pending, success or failed.

**Arguments**:

- `id_or_code`: An ID or code for the batch whose charges you want to retrieve.
- `perPage`: Specify how many records you want to retrieve per page. If not specify we use a default value of 50.
- `page`: Specify exactly what page you want to retrieve. If not specify we use a default value of 1.
- `from_`: A timestamp from which to start listing charges e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
- `to`: A timestamp at which to stop listing charges e.g. 2016-09-24T00:00:05.000Z, 2016-09-21

**Returns**:

Response

<a id="paystack.bulkcharge.BulkCharge.pause_bulk_charge"></a>

#### pause\_bulk\_charge

```python
async def pause_bulk_charge(*, batch_code: str)
```

Use this endpoint to pause processing a batch

**Arguments**:

- `batch_code`: The batch code for the bulk charge you want to pause

**Returns**:

Response

<a id="paystack.bulkcharge.BulkCharge.resume_bulk_charge"></a>

#### resume\_bulk\_charge

```python
async def resume_bulk_charge(*, batch_code: str)
```

Use this endpoint to resume processing a batch

**Arguments**:

- `batch_code`: The batch code for the bulk charge you want to resume

**Returns**:

Response

<a id="paystack.charge"></a>

# paystack.charge

<a id="paystack.charge.Charge"></a>

## Charge Objects

```python
class Charge(Base)
```

The Charge API allows you to configure payment channel of your choice when initiating a payment.

<a id="paystack.charge.Charge.create"></a>

#### create

```python
async def create(*, email: str, amount: str, birthday: str, **kwargs)
```

Initiate a payment by integrating the payment channel of your choice.

**Arguments**:

- `email`: Customer's email address
- `amount`: Amount should be in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR
- `birthday`: 
- `kwargs`: 

**Returns**:

Response

<a id="paystack.charge.Charge.submit_pin"></a>

#### submit\_pin

```python
async def submit_pin(*, pin: str, reference: str)
```

Submit PIN to continue a charge

**Arguments**:

- `pin`: PIN submitted by user
- `reference`: Reference for transaction that requested pin

**Returns**:

Response

<a id="paystack.charge.Charge.submit_otp"></a>

#### submit\_otp

```python
async def submit_otp(*, otp: str, reference: str)
```

Submit OTP to complete a charge

**Arguments**:

- `otp`: OTP submitted by user
- `reference`: Reference for ongoing transaction

**Returns**:

Response

<a id="paystack.charge.Charge.submit_phone"></a>

#### submit\_phone

```python
async def submit_phone(*, phone: str, reference: str)
```

Submit Phone when requested

**Arguments**:

- `phone`: Phone submitted by user
- `reference`: Reference for ongoing transaction

**Returns**:

Response

<a id="paystack.charge.Charge.submit_birthday"></a>

#### submit\_birthday

```python
async def submit_birthday(*, birthday: str, reference: str)
```

Submit Birthday when requested

**Arguments**:

- `birthday`: Birthday submitted by user e.g. 2016-09-21
- `reference`: Reference for ongoing transaction

**Returns**:

Response

<a id="paystack.charge.Charge.submit_address"></a>

#### submit\_address

```python
async def submit_address(*, address: str, reference: str, city: str,
                         state: str, zipcode: str)
```

Submit address to continue a charge

**Arguments**:

- `address`: Address submitted by user
- `reference`: Reference for ongoing transaction
- `city`: City submitted by user
- `state`: State submitted by user
- `zipcode`: Zipcode submitted by user

**Returns**:

Response

<a id="paystack.charge.Charge.check_pending"></a>

#### check\_pending

```python
async def check_pending(*, reference: str)
```

Check Pending Charge

**Arguments**:

- `reference`: The reference to check

**Returns**:

Response

<a id="paystack.control_panel"></a>

# paystack.control\_panel

<a id="paystack.control_panel.ControlPanel"></a>

## ControlPanel Objects

```python
class ControlPanel(Base)
```

The Control Panel API allows you manage some settings on your integration

<a id="paystack.control_panel.ControlPanel.fetch_payment_session_timeout"></a>

#### fetch\_payment\_session\_timeout

```python
async def fetch_payment_session_timeout()
```

Fetch the payment session timeout on your integration

**Returns**:

Response

<a id="paystack.control_panel.ControlPanel.update_payment_session_timeout"></a>

#### update\_payment\_session\_timeout

```python
async def update_payment_session_timeout(*, timeout: int)
```

Update the payment session timeout on your integration

**Arguments**:

- `timeout`: Time before stopping session (in seconds). Set to 0 to cancel session timeouts

**Returns**:

Response

<a id="paystack.customers"></a>

# paystack.customers

<a id="paystack.customers.Customers"></a>

## Customers Objects

```python
class Customers(Base)
```

The Customers API allows you create and manage customers on your integration.

<a id="paystack.customers.Customers.create"></a>

#### create

```python
async def create(*, email: str, last_name: str, first_name: str, **kwargs)
```

Create a customer on your integration

**Arguments**:

- `email`: Customer's email address
- `last_name`: Customer's last name
- `first_name`: Customer's first name
- `kwargs`: Optional params as kwargs

**Returns**:

Response

<a id="paystack.customers.Customers.list"></a>

#### list

```python
async def list(perPage: int = 50,
               page: int = 1,
               from_: datetime | None | str = None,
               to: datetime | None | str = None)
```

List customers available on your integration

**Arguments**:

- `perPage`: Specify how many records you want to retrieve per page. If not specify we use a default value of 50.
- `page`: Specify exactly what page you want to retrieve. If not specify we use a default value of 1.
- `from_`: A timestamp from which to start listing customers e.g.
- `to`: A timestamp at which to stop listing product e.g. 2016-09-24T00:00:05.000Z, 2016-09-21

**Returns**:

Response

<a id="paystack.customers.Customers.fetch"></a>

#### fetch

```python
async def fetch(*, email_or_code: str)
```

Get details of a customer on your integration.

**Arguments**:

- `email_or_code`: An email or customer code for the customer you want to fetch

**Returns**:

Response

<a id="paystack.customers.Customers.update"></a>

#### update

```python
async def update(*, code, first_name: str, last_name: str, **kwargs)
```

Update a customer's details on your integration

**Arguments**:

- `last_name`: Customer's last name
- `first_name`: Customer's first name
- `code`: Customer's code
- `kwargs`: 

**Returns**:

Response

<a id="paystack.customers.Customers.validate"></a>

#### validate

```python
async def validate(*,
                   code: str,
                   last_name: str,
                   first_name: str,
                   value: str,
                   bvn: str,
                   bank_code: str,
                   account_number: str,
                   type: str = "bank_account",
                   country: str = "NG",
                   **kwargs)
```

Validate a customer's identity

**Arguments**:

- `code`: customer_identity code
- `last_name`: Customer's last name
- `first_name`: Customer's first name
- `type`: redefined types of identification. Only bank_account is supported at the moment
- `value`: Customer's identification number
- `country`: 2 letter country code of identification issuer
- `bvn`: Customer's Bank Verification Number
- `bank_code`: You can get the list of Bank Codes by calling the List Banks endpoint. (
required if type is bank_account)
- `account_number`: Customer's bank account number. (required if type is bank_account)
- `kwargs`: Optional params as keyword args

**Returns**:

Response

<a id="paystack.customers.Customers.set_risk_action"></a>

#### set\_risk\_action

```python
async def set_risk_action(*,
                          customer: str,
                          email: str,
                          risk_action: Literal['default', 'deny',
                                               'allow'] = 'default')
```

Whitelist or blacklist a customer on your integration

**Arguments**:

- `email`: Customer email
- `customer`: Customer's code
- `risk_action`: One of the possible risk actions [ default, allow, deny ]. allow to whitelist.
deny to blacklist. Customers start with a default risk action.

**Returns**:

Response

<a id="paystack.customers.Customers.deactivate_authorization"></a>

#### deactivate\_authorization

```python
async def deactivate_authorization(authorization_code: str)
```

Deactivate an authorization when the card needs to be forgotten

**Arguments**:

- `authorization_code`: Authorization code to be deactivated

**Returns**:

Response

<a id="paystack.dedicated_virtual_accounts"></a>

# paystack.dedicated\_virtual\_accounts

<a id="paystack.dedicated_virtual_accounts.DedicatedVirtualAccount"></a>

## DedicatedVirtualAccount Objects

```python
class DedicatedVirtualAccount(Base)
```

The Dedicated Virtual Account API enables Nigerian merchants to manage unique payment accounts of their customers.

<a id="paystack.dedicated_virtual_accounts.DedicatedVirtualAccount.create"></a>

#### create

```python
async def create(*, customer: str, **kwargs)
```

Create a dedicated virtual account and assign to a customer

**Arguments**:

- `customer`: Customer ID or code
- `kwargs`: 

**Returns**:

Response

<a id="paystack.dedicated_virtual_accounts.DedicatedVirtualAccount.assign"></a>

#### assign

```python
async def assign(email: str, first_name: str, last_name: str, phone: str,
                 preferred_bank: str, country: str, **kwargs)
```

With this endpoint, you can create a customer, validate the customer, and assign a DVA to the customer.

**Arguments**:

- `email`: Customer email address
- `first_name`: Customer first name
- `last_name`: Customer last name
- `phone`: Customer phone number
- `preferred_bank`: The bank slug for preferred bank. To get a list of available banks, use the List Providers endpoint
- `country`: Currently accepts NG only
- `kwargs`: Optional parameters

<a id="paystack.dedicated_virtual_accounts.DedicatedVirtualAccount.list"></a>

#### list

```python
async def list(active: bool = True, currency: str = "NGN", **kwargs)
```

List dedicated virtual accounts available on your integration.

**Arguments**:

- `active`: Status of the dedicated virtual account
- `currency`: The currency of the dedicated virtual account. Only NGN is currently allowed
- `kwargs`: Optional parameters

**Returns**:

Response

<a id="paystack.dedicated_virtual_accounts.DedicatedVirtualAccount.fetch"></a>

#### fetch

```python
async def fetch(*, dedicated_account_id)
```

Get details of a dedicated virtual account on your integration.

**Arguments**:

- `dedicated_account_id`: ID of dedicated virtual account

**Returns**:

Response

<a id="paystack.dedicated_virtual_accounts.DedicatedVirtualAccount.deactivate"></a>

#### deactivate

```python
async def deactivate(*, dedicated_account_id)
```

Deactivate a dedicated virtual account on your integration.

**Arguments**:

- `dedicated_account_id`: ID of dedicated virtual account

**Returns**:

Response

<a id="paystack.dedicated_virtual_accounts.DedicatedVirtualAccount.split"></a>

#### split

```python
async def split(customer: str, **kwargs)
```

Split a dedicated virtual account transaction with one or more accounts

**Arguments**:

- `customer`: Customer ID or code
- `kwargs`: 

**Returns**:

Response

<a id="paystack.dedicated_virtual_accounts.DedicatedVirtualAccount.requery"></a>

#### requery

```python
async def requery(*, account_number: str, provider_slug: str, **kwargs)
```

Requery Dedicated Virtual Account for new transactions

**Arguments**:

- `account_number`: Virtual account number to requery
- `provider_slug`: The bank's slug in lowercase, without spaces e.g. wema-bank
- `kwargs`: 

**Returns**:

Response

<a id="paystack.dedicated_virtual_accounts.DedicatedVirtualAccount.remove_split"></a>

#### remove\_split

```python
async def remove_split(*, account_number: str)
```

If you've previously set up split payment for transactions on a dedicated virtual account, you can remove

it with this endpoint

**Arguments**:

- `account_number`: Dedicated virtual account number

**Returns**:

Response

<a id="paystack.dedicated_virtual_accounts.DedicatedVirtualAccount.fetch_providers"></a>

#### fetch\_providers

```python
async def fetch_providers()
```

Get available bank providers for a dedicated virtual account

**Returns**:

Response

<a id="paystack.disputes"></a>

# paystack.disputes

<a id="paystack.disputes.Disputes"></a>

## Disputes Objects

```python
class Disputes(Base)
```

<a id="paystack.disputes.Disputes.list"></a>

#### list

```python
async def list(*, from_: date | str, to: date | str, **kwargs)
```

List disputes filed against you

**Arguments**:

- `from_`: A timestamp from which to start listing dispute e.g. 2016-09-21
- `to`: A timestamp at which to stop listing dispute e.g. 2016-09-21
- `kwargs`: 

**Returns**:

Response

<a id="paystack.disputes.Disputes.fetch"></a>

#### fetch

```python
async def fetch(*, id: str)
```

Get more details about a dispute.

**Arguments**:

- `id`: The dispute ID you want to fetch

**Returns**:

Response

<a id="paystack.disputes.Disputes.list_transaction_disputes"></a>

#### list\_transaction\_disputes

```python
async def list_transaction_disputes(*, id)
```

This endpoint retrieves disputes for a particular transaction

**Arguments**:

- `id`: The transaction ID you want to fetch

**Returns**:

Response

<a id="paystack.disputes.Disputes.update"></a>

#### update

```python
async def update(*, id: str, refund_amount: int, **kwargs)
```

Update details of a dispute on your integration

**Arguments**:

- `id`: 
- `refund_amount`: the amount to refund, in kobo if currency is NGN, pesewas, if currency is GHS,
and cents, if currency is ZAR

**Returns**:

Response

<a id="paystack.disputes.Disputes.add_evidence"></a>

#### add\_evidence

```python
async def add_evidence(*, id: str, customer_email: str, customer_name: str,
                       customer_phone: str, service_details: str, **kwargs)
```

Provide evidence for a dispute

**Arguments**:

- `id`: dispute id
- `customer_email`: Customer Email
- `customer_name`: Customer Name
- `customer_phone`: Customer Phone
- `service_details`: Details of service involved
- `kwargs`: 

**Returns**:

Response

<a id="paystack.disputes.Disputes.get_upload_url"></a>

#### get\_upload\_url

```python
async def get_upload_url(*, id: str, upload_filename: str)
```

Get URL to upload a dispute evidence.

**Arguments**:

- `id`: Dispute Id
- `upload_filename`: The file name, with its extension, that you want to upload. e.g filename.pdf

**Returns**:

Response

<a id="paystack.disputes.Disputes.resolve"></a>

#### resolve

```python
async def resolve(*, id: str, resolution: Literal['merchant-accepted',
                                                  'declined'], message: str,
                  refund_amount: int, uploaded_filename: str, **kwargs)
```

Resolve a dispute on your integration

**Arguments**:

- `id`: Dispute Id
- `resolution`: Dispute resolution. Accepted values: { merchant-accepted | declined }.
- `message`: Reason for resolving
- `refund_amount`: the amount to refund, in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR
- `uploaded_filename`: filename of attachment returned via response from upload url(GET /dispute/:id/upload_url)
- `kwargs`: 

**Returns**:

Response

<a id="paystack.disputes.Disputes.export"></a>

#### export

```python
async def export(*, from_: date | str, to: date | str, **kwargs)
```

Export disputes available on your integration

**Arguments**:

- `from_`: A timestamp from which to start listing dispute e.g. 2016-09-21
- `to`: A timestamp at which to stop listing dispute e.g. 2016-09-21
- `kwargs`: 

**Returns**:

Response

<a id="paystack.invoices"></a>

# paystack.invoices

<a id="paystack.invoices.Invoices"></a>

## Invoices Objects

```python
class Invoices(Base)
```

The Invoices API allows you issue out and manage payment requests

<a id="paystack.invoices.Invoices.create"></a>

#### create

```python
async def create(*, customer: str, amount: int | None = None, **kwargs)
```

Create an invoice for payment on your integration

**Arguments**:

- `customer`: Customer id or code
- `amount`: Payment request amount. It should be used when line items and tax values aren't specified.
- `kwargs`: 

**Returns**:

Response

<a id="paystack.invoices.Invoices.list"></a>

#### list

```python
async def list(customer: str,
               status: str,
               currency: Literal['NGN', 'GHS', 'ZAR', 'USD'],
               include_archive: str,
               from_: datetime | str = "",
               perPage: int = 50,
               page: int = 1,
               **kwargs)
```

List the invoice available on your integration.

**Arguments**:

- `page`: Specify exactly what page you want to retrieve. If not specify we use a default value of 1.
- `perPage`: Specify how many records you want to retrieve per page. If not specify we use a default value of 50.
- `customer`: Filter by customer ID
- `status`: Filter by invoice status
- `currency`: Filter by currency. Allowed values are NGN, GHS, ZAR and USD
- `include_archive`: Show archived invoices
- `from_`: from A timestamp from which to start listing invoice e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
- `kwargs`: 

**Returns**:

Response

<a id="paystack.invoices.Invoices.view"></a>

#### view

```python
async def view(*, id_or_code: str)
```

Get details of an invoice on your integration.

**Arguments**:

- `id_or_code`: The invoice ID or code you want to fetch

**Returns**:

Response

<a id="paystack.invoices.Invoices.verify"></a>

#### verify

```python
async def verify(*, code: str)
```

Verify details of an invoice on your integration.

**Arguments**:

- `code`: Invoice code

**Returns**:

Response

<a id="paystack.invoices.Invoices.send_notification"></a>

#### send\_notification

```python
async def send_notification(*, code: str)
```

**Arguments**:

- `code`: Invoice code

**Returns**:

Response

<a id="paystack.invoices.Invoices.invoice_totals"></a>

#### invoice\_totals

```python
async def invoice_totals()
```

Get invoice metrics for dashboard

**Returns**:

Response

<a id="paystack.invoices.Invoices.finalize_invoice"></a>

#### finalize\_invoice

```python
async def finalize_invoice(*, code: str)
```

Finalize a Draft Invoice

**Arguments**:

- `code`: Invoice code

**Returns**:

Response

<a id="paystack.invoices.Invoices.update"></a>

#### update

```python
async def update(*, id_or_code: str, customer: str, **kwargs)
```

Update an invoice details on your integration

**Arguments**:

- `id_or_code`: Invoice ID or slug
- `customer`: Customer id or code
- `amount`: Payment request amount. Only useful if line items and tax values are ignored. endpoint will throw a friendly warning
if neither is available.
- `kwargs`: 

**Returns**:

Response

<a id="paystack.invoices.Invoices.archive"></a>

#### archive

```python
async def archive(*, id_or_code: str)
```

Used to archive an invoice. Invoice will no longer be fetched on list or returned on verify.

**Arguments**:

- `id_or_code`: Code of the invoice

**Returns**:

Response

<a id="paystack.misc"></a>

# paystack.misc

<a id="paystack.misc.Miscellaneous"></a>

## Miscellaneous Objects

```python
class Miscellaneous(Base)
```

The Miscellaneous API are supporting APIs that can be used to provide more details to other APIs

<a id="paystack.misc.Miscellaneous.list_banks"></a>

#### list\_banks

```python
async def list_banks(*,
                     country: str = "nigeria",
                     use_cursor: bool = True,
                     perPage: int = 50,
                     **kwargs)
```

Get a list of all supported banks and their properties

**Arguments**:

- `country`: The country from which to obtain the list of supported banks. e.g country=ghana or country=nigeria
- `use_cursor`: Flag to enable cursor pagination on the endpoint
- `perPage`: The number of objects to return per page. Defaults to 50, and limited to 100 records per page.
- `kwargs`: 

**Returns**:

Response

<a id="paystack.misc.Miscellaneous.list_providers"></a>

#### list\_providers

```python
async def list_providers()
```

**Returns**:

Response

<a id="paystack.misc.Miscellaneous.list_countries"></a>

#### list\_countries

```python
async def list_countries()
```

Gets a list of Countries that Paystack currently supports

**Returns**:

Response

<a id="paystack.misc.Miscellaneous.list_states"></a>

#### list\_states

```python
async def list_states(*, country: str)
```

Get a list of states for a country for address verification.

**Arguments**:

- `country`: The country code of the states to list. It is gotten after the charge request.

**Returns**:

Response

<a id="paystack.page"></a>

# paystack.page

<a id="paystack.page.PaymentPages"></a>

## PaymentPages Objects

```python
class PaymentPages(Base)
```

The Payment Pages API provides a quick and secure way to collect payment for products.

<a id="paystack.page.PaymentPages.create"></a>

#### create

```python
async def create(*, name: str, **kwargs)
```

Create a payment page on your integration

**Arguments**:

- `name`: Name of page
- `kwargs`: Optional Parameters

**Returns**:

Response

<a id="paystack.page.PaymentPages.list"></a>

#### list

```python
async def list(*,
               perPage: int = 50,
               page: int = 1,
               from_: datetime | str = "",
               to: datetime | str = "")
```

List payment pages available on your integration.

**Arguments**:

- `perPage`: Specify how many records you want to retrieve per page. If not specify we use a default value of 50.
- `page`: Specify exactly what page you want to retrieve. If not specify we use a default value of 1.
- `from_`: A timestamp from which to start listing page e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
- `to`: A timestamp at which to stop listing page e.g. 2016-09-24T00:00:05.000Z, 2016-09-21

**Returns**:

Response

<a id="paystack.page.PaymentPages.fetch"></a>

#### fetch

```python
async def fetch(*, id_or_slug)
```

Get details of a payment page on your integration.

**Arguments**:

- `id_or_slug`: The page ID or slug you want to fetch

**Returns**:

Response

<a id="paystack.page.PaymentPages.update"></a>

#### update

```python
async def update(*, id_or_slug: str, name: str, description: str, **kwargs)
```

Update a payment page details on your integration

**Arguments**:

- `id_or_slug`: Page ID or slug
- `name`: Name of page
- `description`: A description for this page
- `kwargs`: 

**Returns**:

Response

<a id="paystack.page.PaymentPages.is_slug_available"></a>

#### is\_slug\_available

```python
async def is_slug_available(*, slug)
```

Check the availability of a slug for a payment page.

**Arguments**:

- `slug`: URL slug to be confirmed

**Returns**:

Response

<a id="paystack.page.PaymentPages.add_products"></a>

#### add\_products

```python
async def add_products(*, id: int, product: List[int])
```

Add products to a payment page

**Arguments**:

- `id`: Id of the payment page
- `product`: Ids of all the products

**Returns**:

Response

<a id="paystack.paystack"></a>

# paystack.paystack

<a id="paystack.plans"></a>

# paystack.plans

<a id="paystack.plans.Plans"></a>

## Plans Objects

```python
class Plans(Base)
```

The Plans API allows you create and manage installment payment options on your integration

<a id="paystack.plans.Plans.create"></a>

#### create

```python
async def create(*, name: str, amount: int,
                 interval: Literal['daily', 'weekly', 'monthly', 'biannually',
                                   'annually'], **kwargs)
```

Create a plan on your integration

**Arguments**:

- `name`: Name of plan
- `amount`: Amount should be in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR
- `interval`: Interval in words. Valid intervals are: daily, weekly, monthly,biannually, annually.
- `kwargs`: Optional keyword args to form the body of the request

**Returns**:

Json data from paystack API.

<a id="paystack.plans.Plans.list"></a>

#### list

```python
async def list(perPage: int = 50, page: int = 1, **kwargs)
```

List plans available on your integration.

**Arguments**:

- `perPage`: Specify how many records you want to retrieve per page.
- `page`: Specify exactly what page you want to retrieve.
- `kwargs`: Keyword args to form the query params

**Returns**:

Response

<a id="paystack.plans.Plans.fetch"></a>

#### fetch

```python
async def fetch(*, id_or_code: str)
```

Get details of a plan on your integration.

**Arguments**:

- `id_or_code`: The plan ID or code you want to fetch

**Returns**:

Response

<a id="paystack.plans.Plans.update"></a>

#### update

```python
async def update(*, id_or_code: str, name: str, amount: int,
                 interval: Literal['daily', 'weekly', 'monthly', 'biannually',
                                   'annually'], **kwargs)
```

Update a plan details on your integration

**Arguments**:

- `id_or_code`: Plan's ID or code
- `name`: Name of plan
- `amount`: Amount should be in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR
- `interval`: Interval in words. Valid intervals are: daily, weekly, monthly,biannually, annually.
- `kwargs`: Optional keyword args to form the body of the request

**Returns**:

Response

<a id="paystack.products"></a>

# paystack.products

<a id="paystack.products.Products"></a>

## Products Objects

```python
class Products(Base)
```

The Products API allows you create and manage inventories on your integration

<a id="paystack.products.Products.create"></a>

#### create

```python
async def create(*, name: str, description: str, price: int, currency: str,
                 **kwargs)
```

Create a product on your integration

**Arguments**:

- `name`: Name of product
- `description`: A description for this product
- `price`: Price should be in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR
- `currency`: Currency in which price is set. Allowed values are: NGN, GHS, ZAR or USD

**Returns**:

Response

<a id="paystack.products.Products.list"></a>

#### list

```python
async def list(perPage: int = 50,
               page: int = 1,
               from_: datetime | None | str = None,
               to: datetime | None | str = None)
```

List products available on your integration.

**Arguments**:

- `perPage`: Specify how many records you want to retrieve per page. If not specify we use a default value of 50.
- `page`: Specify exactly what page you want to retrieve. If not specify we use a default value of 1.
- `from_`: A timestamp from which to start listing product e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
- `to`: A timestamp at which to stop listing product e.g. 2016-09-24T00:00:05.000Z, 2016-09-21

**Returns**:

Response

<a id="paystack.products.Products.fetch"></a>

#### fetch

```python
async def fetch(*, id: str)
```

Get details of a product on your integration.

**Arguments**:

- `id`: The product ID you want to fetch

**Returns**:

Response

<a id="paystack.products.Products.update"></a>

#### update

```python
async def update(*, id: str, name: str, description: str, price: int,
                 currency: str, **kwargs)
```

Update a product details on your integration

**Arguments**:

- `id`: Product ID
- `name`: Name of product
- `description`: A description for this product
- `price`: Price should be in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR
- `currency`: Currency in which price is set. Allowed values are: NGN, GHS, ZAR or USD
- `kwargs`: 

**Returns**:

Response

<a id="paystack.refund"></a>

# paystack.refund

<a id="paystack.refund.Refund"></a>

## Refund Objects

```python
class Refund(Base)
```

The Refunds API allows you create and manage transaction refunds

<a id="paystack.refund.Refund.create"></a>

#### create

```python
async def create(*, transaction: str, **kwargs)
```

Initiate a refund on your integration

**Arguments**:

- `transaction`: Transaction reference or id
- `kwargs`: 

**Returns**:

Response

<a id="paystack.refund.Refund.list"></a>

#### list

```python
async def list(*, reference: str, currency: Literal['NGN', 'GHS', 'ZAR',
                                                    'USD'], **kwargs)
```

List refunds available on your integration.

**Arguments**:

- `reference`: Identifier for transaction to be refunded
- `currency`: Three-letter ISO currency. Allowed values are: NGN, GHS, ZAR or USD
- `kwargs`: 

**Returns**:

Response

<a id="paystack.refund.Refund.fetch"></a>

#### fetch

```python
async def fetch(*, reference: str)
```

Get details of a refund on your integration.

**Arguments**:

- `reference`: Identifier for transaction to be refunded

**Returns**:

Response

<a id="paystack.settlements"></a>

# paystack.settlements

<a id="paystack.settlements.Settlements"></a>

## Settlements Objects

```python
class Settlements(Base)
```

The Settlements API allows you gain insights into payouts made by Paystack to your bank account

<a id="paystack.settlements.Settlements.fetch"></a>

#### fetch

```python
async def fetch(*,
                perPage: int = 50,
                page: int = 1,
                subaccount: str = 'none',
                from_: datetime | None | str = None,
                to: datetime | None | str = None)
```

**Arguments**:

- `page`: Specify exactly what page you want to retrieve. If not specify we use a default value of 1.
- `perPage`: Specify how many records you want to retrieve per page. If not specify we use a default value of 50.
- `subaccount`: Provide a subaccount ID to export only settlements for that subaccount. Set to none to export only transactions for the
account.
- `from_`: A timestamp from which to start listing settlements e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
- `to`: A timestamp at which to stop listing settlements e.g. 2016-09-24T00:00:05.000Z, 2016-09-21

<a id="paystack.settlements.Settlements.fetch_settlement_transactions"></a>

#### fetch\_settlement\_transactions

```python
async def fetch_settlement_transactions(*,
                                        perPage: int = 50,
                                        page: int = 1,
                                        from_: datetime | None | str = None,
                                        to: datetime | None | str = None)
```

**Arguments**:

- `page`: Specify exactly what page you want to retrieve. If not specify we use a default value of 1.
- `perPage`: Specify how many records you want to retrieve per page. If not specify we use a default value of 50.
- `from_`: A timestamp from which to start listing settlement transactions e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
- `to`: A timestamp at which to stop listing settlement transactions e.g. 2016-09-24T00:00:05.000Z, 2016-09-21

<a id="paystack.subaccounts"></a>

# paystack.subaccounts

<a id="paystack.subaccounts.SubAccounts"></a>

## SubAccounts Objects

```python
class SubAccounts(Base)
```

The Subaccounts API allows you create and manage subaccounts on your integration.
Subaccounts can be used to split payment between two accounts (your main account and a sub account)

<a id="paystack.subaccounts.SubAccounts.create"></a>

#### create

```python
async def create(*,
                 business_name: str,
                 settlement_bank: str,
                 account_number: str,
                 percentage_charge: float,
                 description: str = "",
                 **kwargs)
```

Create a subacount on your integration

**Arguments**:

- `description`: A description for this subaccount
- `percentage_charge`: A description for this subaccount
- `account_number`: Bank Account Number
- `settlement_bank`: Bank Code for the bank. You can get the list of Bank Codes by calling the List Banks endpoint.
- `business_name`: Name of business for subaccount
- `kwargs`: 

**Returns**:

Response

<a id="paystack.subaccounts.SubAccounts.list"></a>

#### list

```python
async def list(*,
               perPage: int = 50,
               page: int = 1,
               from_: datetime | None | str = None,
               to: datetime | None | str = None)
```

List subaccounts available on your integration.

**Arguments**:

- `perPage`: Specify how many records you want to retrieve per page. If not specify we use a default value of 50.
- `page`: Specify exactly what page you want to retrieve. If not specify we use a default value of 1.
- `to`: A timestamp at which to stop listing subaccounts e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
- `from_`: A timestamp from which to start listing subaccounts e.g. 2016-09-24T00:00:05.000Z, 2016-09-21

**Returns**:

Response

<a id="paystack.subaccounts.SubAccounts.fetch"></a>

#### fetch

```python
async def fetch(*, id_or_code: str)
```

Get details of a subaccount on your integration

**Arguments**:

- `id_or_code`: The subaccount ID or code you want to fetch

**Returns**:

Response

<a id="paystack.subaccounts.SubAccounts.update"></a>

#### update

```python
async def update(*, id_or_code: str, business_name: str, settlement_bank: str,
                 account_number: str, **kwargs)
```

Update a subaccount details on your integration

**Arguments**:

- `settlement_bank`: Bank Code for the bank. You can get the list of Bank Codes by calling the List Banks endpoint.
- `business_name`: Name of business for subaccount
- `id_or_code`: Subaccount's ID or code
- `account_number`: Bank Account Number
- `kwargs`: 

**Returns**:

Response

<a id="paystack.subscriptions"></a>

# paystack.subscriptions

<a id="paystack.subscriptions.Subscriptions"></a>

## Subscriptions Objects

```python
class Subscriptions(Base)
```

The Subscriptions API allows you create and manage recurring payment on your integration

<a id="paystack.subscriptions.Subscriptions.create"></a>

#### create

```python
async def create(*,
                 customer: str,
                 plan: str,
                 authorization: str = "",
                 start_date: str = "")
```

Create a subscription on your integration

**Arguments**:

- `customer`: Customer's email address or customer code
- `plan`: Plan code
- `authorization`: If customer has multiple authorizations, you can set the desired authorization you wish to use for this subscription
here. If this is not supplied, the customer's most recent authorization would be used
- `start_date`: Set the date for the first debit. (ISO 8601 format) e.g. 2017-05-16T00:30:13+01:00

**Returns**:

Response

<a id="paystack.subscriptions.Subscriptions.list"></a>

#### list

```python
async def list(*,
               perPage: int = 50,
               page: int = 1,
               customer: int | None = None,
               plan: int | None = None)
```

List subscriptions available on your integration.

**Arguments**:

- `page`: Specify exactly what page you want to retrieve. If not specify we use a default value of 1.
- `perPage`: Specify how many records you want to retrieve per page. If not specify we use a default value of 50.
- `customer`: Filter by Customer ID
- `plan`: Filter by Plan ID

**Returns**:

Response

<a id="paystack.subscriptions.Subscriptions.fetch"></a>

#### fetch

```python
async def fetch(*, id_or_code: str)
```

Get details of a subscription on your integration.

**Arguments**:

- `id_or_code`: The subscription ID or code you want to fetch

**Returns**:

Response

<a id="paystack.subscriptions.Subscriptions.enable"></a>

#### enable

```python
async def enable(code: str, token: str)
```

Enable a subscription on your integration

**Arguments**:

- `code`: Subscription code
- `token`: Email token

**Returns**:

Response

<a id="paystack.subscriptions.Subscriptions.disable"></a>

#### disable

```python
async def disable(*, code: str, token: str)
```

Disable a subscription on your integration

**Arguments**:

- `code`: Subscription code
- `token`: Email token

**Returns**:

Response

<a id="paystack.subscriptions.Subscriptions.generate_update_subscription_link"></a>

#### generate\_update\_subscription\_link

```python
async def generate_update_subscription_link(*, code)
```

Generate a link for updating the card on a subscription

**Arguments**:

- `code`: Subscription code

**Returns**:

Response

<a id="paystack.subscriptions.Subscriptions.send_update_subscription_link"></a>

#### send\_update\_subscription\_link

```python
async def send_update_subscription_link(*, code)
```

Email a customer a link for updating the card on their subscription

**Arguments**:

- `code`: Subscription code

**Returns**:

Response

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

<a id="paystack.transaction_splits"></a>

# paystack.transaction\_splits

<a id="paystack.transaction_splits.TransactionSplits"></a>

## TransactionSplits Objects

```python
class TransactionSplits(Base)
```

The Transaction Splits API enables merchants split the settlement for a transaction across their payout account,
and one or more Subaccounts.

<a id="paystack.transaction_splits.TransactionSplits.create"></a>

#### create

```python
async def create(*, name: str, type: Literal['percentage', 'flat'],
                 currency: Literal['NGN', 'GHS', 'ZAR',
                                   'USD'], subaccounts: list[dict],
                 bearer_type: Literal['subaccount', 'account',
                                      'all-proportional',
                                      'all'], bearer_subaccount: str)
```

Create a split payment on your integration

**Arguments**:

- `name`: Name of the transaction split
- `type`: The type of transaction split you want to create. You can use one of the following: percentage | flat
- `currency`: Any of NGN, GHS, ZAR, or USD
- `subaccounts`: A list of object containing subaccount code and number of shares:[{subaccount: ‘ACT_xxxxxxxxxx’, share: xxx},{...}]
- `bearer_type`: Any of subaccount | account | all-proportional | all
- `bearer_subaccount`: Subaccount code

**Returns**:

Response

<a id="paystack.transaction_splits.TransactionSplits.list"></a>

#### list

```python
async def list(name: str,
               active: bool,
               from_: datetime | None | str = None,
               **kwargs)
```

List/search for the transaction splits available on your integration.

**Arguments**:

- `name`: The name of the split
- `active`: Any of true or false
- `from_`: A timestamp from which to start listing splits, the optional "from" argument is to be added this way with a trailing underscore
- `kwargs`: Optional keyword query parameters as keyword args

**Returns**:

Response

<a id="paystack.transaction_splits.TransactionSplits.search"></a>

#### search

```python
async def search(name: str,
                 active: bool,
                 from_: datetime | None | str = None,
                 **kwargs)
```

Does the exact same thing as list

**Arguments**:

- `name`: The name of the split
- `active`: Any of true or false
- `from_`: A timestamp from which to start listing splits, the optional from argument is to be added this way with a trailing underscore
- `kwargs`: Optional keyword query parameters as keyword args

**Returns**:

Response

<a id="paystack.transaction_splits.TransactionSplits.fetch"></a>

#### fetch

```python
async def fetch(*, id: str)
```

Get details of a split on your integration

**Arguments**:

- `id`: The id of the split

**Returns**:

Response

<a id="paystack.transaction_splits.TransactionSplits.update"></a>

#### update

```python
async def update(*, id: str, name: str, active: bool, **kwargs)
```

Update a transaction split details on your integration

**Arguments**:

- `id`: Split ID
- `name`: The name of the split
- `active`: Any of true or false
- `kwargs`: Optional Parameters

**Returns**:

Response

<a id="paystack.transaction_splits.TransactionSplits.add_split_subaccount"></a>

#### add\_split\_subaccount

```python
async def add_split_subaccount(*, id: str, subaccount: str, share: int)
```

Add a Subaccount to a Transaction Split, or update the share of an existing Subaccount in a Transaction Split

**Arguments**:

- `id`: Split Id
- `subaccount`: This is the sub account code
- `share`: This is the transaction share for the subaccount

<a id="paystack.transaction_splits.TransactionSplits.remove_subaccount_from_split"></a>

#### remove\_subaccount\_from\_split

```python
async def remove_subaccount_from_split(*, id: str, subaccount: str)
```

Remove a subaccount from a transaction split

**Arguments**:

- `id`: Split Id
- `subaccount`: This is the sub account code

<a id="paystack.transfers"></a>

# paystack.transfers

<a id="paystack.transfers.Transfers"></a>

## Transfers Objects

```python
class Transfers(Base)
```

The Transfers API allows you automate sending money to your customers

<a id="paystack.transfers.Transfers.initiate"></a>

#### initiate

```python
async def initiate(source: str, amount: int, recipient: str, **kwargs)
```

Status of transfer object returned will be pending if OTP is disabled. In the event that an OTP is required, status will read otp.

**Arguments**:

- `source`: Where should we transfer from? Only balance for now
- `amount`: Amount to transfer in kobo if currency is NGN and pesewas if currency is GHS.
- `recipient`: Code for transfer recipient
- `kwargs`: Optional Parameters

**Returns**:

Response

<a id="paystack.transfers.Transfers.finalize"></a>

#### finalize

```python
async def finalize(*, transfer_code: str, otp: str)
```

Finalize an initiated transfer

**Arguments**:

- `transfer_code`: The transfer code you want to finalize
- `otp`: OTP sent to business phone to verify transfer

**Returns**:

Response

<a id="paystack.transfers.Transfers.initiate_bulk_transfer"></a>

#### initiate\_bulk\_transfer

```python
async def initiate_bulk_transfer(*, source: str,
                                 transfers: list[dict['amount', 'recipient',
                                                      'reference']], **kwargs)
```

You need to disable the Transfers OTP requirement to use this endpoint.

**Arguments**:

- `source`: Where should we transfer from? Only balance for now
- `transfers`: A list of transfer object. Each object should contain

**Returns**:

Response

<a id="paystack.transfers.Transfers.list"></a>

#### list

```python
async def list(*,
               customer: str,
               perPage: int = 50,
               page: int = 1,
               from_: datetime | None | str = None,
               to: datetime | None | str = None,
               **kwargs)
```

List the transfers made on your integration.

**Arguments**:

- `customer`: Filter by customer ID
- `perPage`: Specify how many records you want to retrieve per page. If not specify we use a default value of 50.
- `page`: Specify exactly what transfer you want to page. If not specify we use a default value of 1.
- `from_`: A timestamp from which to start listing transfer e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
- `to`: A timestamp at which to stop listing transfer e.g. 2016-09-24T00:00:05.000Z, 2016-09-21

**Returns**:

Response

<a id="paystack.transfers.Transfers.fetch"></a>

#### fetch

```python
async def fetch(*, id_or_code: str)
```

Get details of a transfer on your integration.

**Arguments**:

- `id_or_code`: The transfer ID or code you want to fetch

**Returns**:

Response

<a id="paystack.transfers.Transfers.verify"></a>

#### verify

```python
async def verify(*, reference: str)
```

Verify the status of a transfer on your integration.

**Arguments**:

- `reference`: Verify the status of a transfer on your integration.

**Returns**:

Response

<a id="paystack.transfer_control"></a>

# paystack.transfer\_control

<a id="paystack.transfer_control.TransferControl"></a>

## TransferControl Objects

```python
class TransferControl(Base)
```

The Transfers Control API allows you manage settings of your transfers

<a id="paystack.transfer_control.TransferControl.check_balance"></a>

#### check\_balance

```python
async def check_balance()
```

Fetch the available balance on your integration

**Returns**:

Response

<a id="paystack.transfer_control.TransferControl.fetch_balance_ledger"></a>

#### fetch\_balance\_ledger

```python
async def fetch_balance_ledger()
```

Fetch all pay-ins and pay-outs that occured on your integration

**Returns**:

Response

<a id="paystack.transfer_control.TransferControl.resend_transfer_otp"></a>

#### resend\_transfer\_otp

```python
async def resend_transfer_otp(*, transfer_code: str,
                              reason: Literal['resend_otp', 'transfer'])
```

Generates a new OTP and sends to customer in the event they are having trouble receiving one.

**Arguments**:

- `transfer_code`: Transfer code
- `reason`: Either resend_otp or transfer

**Returns**:

Response

<a id="paystack.transfer_control.TransferControl.disable_transfers_otp"></a>

#### disable\_transfers\_otp

```python
async def disable_transfers_otp()
```

This is used in the event that you want to be able to complete transfers programmatically without use of OTPs. No arguments required.

You will get an OTP to complete the request.

**Returns**:

Response

<a id="paystack.transfer_control.TransferControl.finalize_disable_otp"></a>

#### finalize\_disable\_otp

```python
async def finalize_disable_otp(*, otp: str)
```

Finalize the request to disable OTP on your transfers.

**Arguments**:

- `otp`: OTP sent to business phone to verify disabling OTP requirement

**Returns**:

Response

<a id="paystack.transfer_control.TransferControl.enable_transfers_otp"></a>

#### enable\_transfers\_otp

```python
async def enable_transfers_otp()
```

In the event that a customer wants to stop being able to complete transfers programmatically, this endpoint helps turn

OTP requirement back on. No arguments required.

**Returns**:

Response

<a id="paystack.transfer_recipient"></a>

# paystack.transfer\_recipient

<a id="paystack.transfer_recipient.TransferRecipient"></a>

## TransferRecipient Objects

```python
class TransferRecipient(Base)
```

The Transfer Recipients API allows you create and manage beneficiaries that you send money to

<a id="paystack.transfer_recipient.TransferRecipient.create"></a>

#### create

```python
async def create(type: Literal['nuban', 'mobile_money', 'basa'],
                 name: str,
                 account_number: str = "",
                 bank_code: str = "",
                 **kwargs)
```

Creates a new recipient. A duplicate account number will lead to the retrieval of the existing record.

**Arguments**:

- `type`: Recipient Type. It could be one of: nuban, mobile_money or basa
- `name`: A name for the recipient
- `account_number`: Required if type is nuban or basa
- `bank_code`: Required if type is nuban or basa. You can get the list of Bank Codes by calling the List Banks endpoint.
- `kwargs`: Optional Parameters

**Returns**:

Response

<a id="paystack.transfer_recipient.TransferRecipient.bulk_create"></a>

#### bulk\_create

```python
async def bulk_create(*, batch: list[dict])
```

Create multiple transfer recipients in batches. A duplicate account number will lead to the retrieval of the existing record.

**Arguments**:

- `batch`: A list of transfer recipient object. Each object should contain type, name, and bank_code.
Any Create Transfer Recipient param can also be passed.

**Returns**:

Response

<a id="paystack.transfer_recipient.TransferRecipient.list"></a>

#### list

```python
async def list(*,
               perPage: int = 50,
               page: int = 1,
               from_: datetime | None | str = None,
               to: datetime | None | str = None)
```

List transfer recipients available on your integration

**Arguments**:

- `page`: Specify exactly what page you want to retrieve. If not specify we use a default value of 1.
- `perPage`: Specify how many records you want to retrieve per page. If not specify we use a default value of 50.
- `from_`: A timestamp from which to start listing transfer recipients e.g. 2016-09-24T00:00:05.000Z, 2016-09-21
- `to`: A timestamp at which to stop listing transfer recipients e.g. 2016-09-24T00:00:05.000Z, 2016-09-21

**Returns**:

Response

<a id="paystack.transfer_recipient.TransferRecipient.fetch"></a>

#### fetch

```python
async def fetch(*, id_or_code)
```

Fetch the details of a transfer recipient

**Arguments**:

- `id_or_code`: An ID or code for the recipient whose details you want to receive

**Returns**:

Response

<a id="paystack.transfer_recipient.TransferRecipient.update"></a>

#### update

```python
async def update(*, id_or_code: str, name: str, email: str = "")
```

Update an existing recipient. Any duplicate account number will lead to the retrieval of the existing record.

**Arguments**:

- `id_or_code`: 
- `name`: A name for the recipient
- `email`: Email address of the recipient

**Returns**:

Response

<a id="paystack.transfer_recipient.TransferRecipient.delete_transfer_recipient"></a>

#### delete\_transfer\_recipient

```python
async def delete_transfer_recipient(*, id_or_code: str)
```

Deletes a transfer recipient (sets the transfer recipient to inactive)

**Arguments**:

- `id_or_code`: Transfer Recipient

**Returns**:

Response

<a id="paystack.verification"></a>

# paystack.verification

<a id="paystack.verification.Verification"></a>

## Verification Objects

```python
class Verification(Base)
```

The Verification API allows you perform KYC processes

<a id="paystack.verification.Verification.resolve_account_number"></a>

#### resolve\_account\_number

```python
async def resolve_account_number(*, account_number: str, bank_code: str,
                                 **kwargs)
```

Confirm an account belongs to the right customer

**Arguments**:

- `account_number`: Account Number
- `bank_code`: You can get the list of bank codes by calling the List Bank endpoint
- `kwargs`: Optional Parameters

**Returns**:

Response

<a id="paystack.verification.Verification.validate_account"></a>

#### validate\_account

```python
async def validate_account(
        *, account_name: str, account_number: str,
        account_type: Literal['personal',
                              'business'], bank_code: str, country_code: str,
        document_type: Literal['identityNumber', 'passportNumber',
                               'businessRegistrationNumber'], **kwargs)
```

Confirm the authenticity of a customer's account number before sending money

**Arguments**:

- `account_name`: Customer's first and last name registered with their bank
- `account_number`: Customer's account number
- `account_type`: This can take one of: [ personal, business ]
- `bank_code`: The bank code of the customer's bank. You can fetch the bank codes by using our List Bank endpoint
- `country_code`: 
- `document_type`: This could be one of: [ identityNumber, passportNumber, businessRegistrationNumber ]
- `kwargs`: Optional Parameters

**Returns**:

Response

<a id="paystack.verification.Verification.resolve_card_bin"></a>

#### resolve\_card\_bin

```python
async def resolve_card_bin(*, bin: str)
```

Get more information about a customer's card

**Arguments**:

- `bin`: First 6 characters of card

**Returns**:

Response

