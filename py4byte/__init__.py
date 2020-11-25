__version__="0.1.0"
__author__="Mike Shultz"
__email__="shultzm@gmail.com"

from .api import signatures

def receipt_events(receipt):
    """ Resolve events in a receipt """
    if not receipt['logs']:
        return []

    event_signatures = []

    for hex_sig in [log['topics'][0][0:10] for log in receipt['logs']]:
        res = signatures(hex_signature=hex_sig)
        if res:
            event_signatures.append(res)

    return event_signatures

def transaction_call(transaction):
    """ Get the function signature for a transaction """
    pass
