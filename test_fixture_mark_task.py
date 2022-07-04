from multiprocessing import Condition
import pytest

@pytest.mark.xfail(strict = 1) #failed if inexpected pass
def test_succeed():
    assert True


@pytest.mark.xfail
def test_not_succeed():
    assert False


@pytest.mark.skip
def test_skipped():
    assert False