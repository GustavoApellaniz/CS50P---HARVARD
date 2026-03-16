from bank import value
import pytest


def test_bank():
    assert value('hello') == 0

def test_bank_int():
    with pytest.raises(TypeError):
        value(432)

def test_bank_20():
    assert value('hi man') == 20 


def test_bank_100():
    assert value('good morning man') == 100 