import pytest

@pytest.mark.xfail(strict=True) #marks a test that should fail but passes as "Failed"
def test_succeed():
    assert True


@pytest.mark.xfail
def test_not_succeed():
    assert False


@pytest.mark.skip
def test_skipped():
    assert False
