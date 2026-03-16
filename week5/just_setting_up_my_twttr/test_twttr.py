from twttr import shorten
import pytest

def test_twttr():
    assert shorten('aRROz') == 'rrz'


def test_twttr_int():
    with pytest.raises(AttributeError):
        shorten(4)
