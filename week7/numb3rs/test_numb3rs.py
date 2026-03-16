from numb3rs import validate
import pytest

def test_numb3rs_limit():
    assert validate('345.545.234.1234') == 'invalid'

def test_numb3rs():
    assert validate('255.255.255.255') == 'valid'

def test_numb3rs_5dots():
    assert validate('35.55.24.123.45') == 'invalid'

def test_numb3rs_4ele():
    assert validate('3435.5245.1234.1234') == 'invalid'
    