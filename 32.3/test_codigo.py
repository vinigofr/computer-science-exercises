from codigo import id_odd

def test_verify_if_odd():
    'odd'
    assert id_odd(3) is True

def test_verify_if_even():
    'even'
    assert id_odd(2) is False
