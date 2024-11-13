import pytest
from pytest_bdd import given, when, then, parsers, scenarios

scenarios("calculator.feature")

class Calculator:
    def __init__ (self):
        self.clear()

    def clear (self):
        self.result = 0

    def add (self, number):
        self.result += int(number)


@pytest.fixture
def calc ():
    return Calculator()

@given("the calculator is cleared")
def clear(calc):
    calc.clear()

@when(parsers.parse("I add {number}"))
def add(calc, number):
    calc.add(number)

@then(parsers.parse("the result should be {result}"))
def check_result(calc, result):
    assert calc.result == int(result)
