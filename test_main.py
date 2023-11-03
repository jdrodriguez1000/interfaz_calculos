import pytest
from main_interface import interface


@pytest.fixture
def main_test():
    return interface()


def test_add_operation_ok(main_test):
    number_1 = 2 
    number_2 = 3
    assert main_test.add_operation(number_1, number_2) == 5

def test_add_operation_string():
    pass