import pytest

@pytest.mark.match
def test_check_math():
    assert 7 * 7 == 49

@pytest.mark.match
def test_check_78():
    assert 7 * 8 == 56