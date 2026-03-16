from seasons import time_life,padrao_data
import pytest


def test_time():
    assert time_life(padrao_data('2005-10-14')) == 'ten million, seven hundred thirty-five thousand, two hundred'

def test_time_wrong():
    with pytest.raises(TypeError):
        time_life(padrao_data('2017, january 17'))