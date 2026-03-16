from plate import is_valid


def test_is_valid():
    assert is_valid('45njjb3') == False

def test_is_valid_2():
    assert is_valid('ab50') == True

def test_is_valid_3():
    assert is_valid('CS50') == True

def test_is_valid_4():
    assert is_valid('dk342034j') == False