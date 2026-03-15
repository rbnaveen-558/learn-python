# Pytest Class Example with Setup and Teardown
import pytest

class TestMath:
    @classmethod
    def setup_class(cls):
        print("\n[Setup class]")
        cls.shared = 10

    @classmethod
    def teardown_class(cls):
        print("[Teardown class]")
        del cls.shared

    def setup_method(self, method):
        print(f"[Setup method] {method.__name__}")
        self.value = 5

    def teardown_method(self, method):
        print(f"[Teardown method] {method.__name__}")
        del self.value

    def test_add(self):
        assert self.value + self.shared == 15

    def test_subtract(self):
        assert self.shared - self.value == 5

    def test_multiply(self):
        assert self.value * 2 == 10
