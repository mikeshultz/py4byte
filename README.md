# py4byte

Library for using 4byte and blind-decoding of transactions and events

## Functions

### signatures(kwargs)

Resolve signatures using the 4byte directory.

#### Arguments

These are the same arguments for the [4byte.directory REST API](https://www.4byte.directory/docs/)

- `text_signature`
- `text_signature__iexact`
- `text_signature__contains`
- `text_signature__icontains`
- `text_signature__startswith`
- `text_signature__istartswith`
- `text_signature__endswith`
- `text_signature__iendswith`
- `hex_signature`

### receipt_events(receipt)

Given a Web3 or JSON-like transaction receipt, attempt to decode events to a text signature.

### transaction_call(transaction)

Given a Web3 or JSON-like transaction, attempt to decode the function signature of a contract call.
