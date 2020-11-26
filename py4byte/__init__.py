from .api import signatures
from .meta import __version__, __author__, __email__  # noqa: F401


def receipt_events(receipt):
    """ Resolve events in a receipt

    Returns list of tuples of [(hex_signature, text_signature)]
    """

    if not receipt['logs']:
        return []

    event_signatures = []

    for hex_sig in [log['topics'][0][0:10] for log in receipt['logs']]:
        res = signatures(hex_signature=hex_sig)
        if res:
            for match in res:
                event_signatures.append((hex_sig, match.get('text_signature')))
        else:
            # Include the ones we don't know bout
            event_signatures.append((hex_sig, None))

    return event_signatures


def transaction_call(transaction):
    """ Get the function signature for a transaction

    Returns a list of text signatures matching the function signature
    """
    tx_input = transaction.get('input')

    if not tx_input or len(tx_input) < 10:
        return None

    hex_sig = tx_input[0:10]

    return [x.get('text_signature') for x in signatures(hex_signature=hex_sig)]
