from working import convert

def test_work():
    assert convert('9 to 5') == '9:00 to 17:00'
def test_work_AMPM():
    assert convert('10 AM to 8:50 PM') == '10:00 to 20:50'
    