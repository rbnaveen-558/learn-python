# Pytest Advanced Features Example
import pytest

# Custom fixture scope
@pytest.fixture(scope="module")
def module_resource():
    print("Setup module resource")
    yield "resource"
    print("Teardown module resource")

def test_module_resource(module_resource):
    assert module_resource == "resource"

# Using tmp_path fixture for file operations
def test_tmp_path(tmp_path):
    file = tmp_path / "test.txt"
    file.write_text("pytest rocks!")
    assert file.read_text() == "pytest rocks!"

# Custom markers
@pytest.mark.slow
def test_slow():
    import time
    time.sleep(1)
    assert True

# Hook example: conftest.py can define hooks like pytest_runtest_setup
# See pytest docs for more details
