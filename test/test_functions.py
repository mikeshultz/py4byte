from py4byte import receipt_events, transaction_call

from .const import SWAP_TRANSACTION, SWAP_RECEIPT


def has_text_sig(decoded, text_sig):
    for d in decoded:
        if d[1] == text_sig:
            return True
    return False


def count_text_sig(decoded, text_sig):
    count = 0
    for d in decoded:
        if d[1] == text_sig:
            count += 1
    return count


def test_receipt_events():
    events = receipt_events(SWAP_RECEIPT)
    assert len(events) == 7, "Unexpected amount of events"
    assert has_text_sig(events, 'Transfer(address,address,uint256)'), "Expected a Transfer event"
    assert count_text_sig(events, 'Transfer(address,address,uint256)') == 3, "Expected 3 Tranfer events"


def test_transaction_call():
    func_sigs = transaction_call(SWAP_TRANSACTION)
    assert func_sigs is not None, "Expected resolution"
    assert len(func_sigs) == 1, "Expected one result (new collision?)"
    assert func_sigs[0] == 'swapExactTokensForTokens(uint256,uint256,address[],address,uint256)', "Expected swapExactTokensForTokens"
