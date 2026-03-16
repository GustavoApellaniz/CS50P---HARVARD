from fuel import convert, gauge


def test_fuel():
    assert gauge(convert('3/4')) == '75%'

def test_fuel_E():
    assert gauge(convert('0/4') == 'E')


