# Pytest Core Features Example
import pytest

def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

# Using fixtures
@pytest.fixture
def sample_data():
    return [1, 2, 3]

def test_sample_data(sample_data):
    assert len(sample_data) == 3

# Marking tests
@pytest.mark.skip(reason="Skip this test")
def test_skip():
    assert False

@pytest.mark.xfail(reason="Expected to fail")
def test_xfail():
    assert 1 == 2
