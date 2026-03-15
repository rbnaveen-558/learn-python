# Pytest Parametrize Example
import pytest

@pytest.mark.parametrize("a,b,result", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0)
])
def test_add_param(a, b, result):
    assert a + b == result



@pytest.mark.parametrize("inp,result", [
    ("ajsbd", 5),
    ("hello", 5),
    ("", 0)
])
def test_count(inp, result):
    assert len(inp) == result