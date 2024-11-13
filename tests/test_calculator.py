from pytest_bdd import given, when, then, parsers, scenarios
from pytest_class_fixtures import class_fixture

scenarios("calculator.feature")

@class_fixture(name="calc")
class Calculator:
    def __init__ (self):
        self.clear()

    def clear (self):
        self.result = 0

    def add (self, number):
        self.result += int(number)

@given("the calculator is cleared")
def clear(calc):
    calc.clear()

@when(parsers.parse("I add {number}"))
def add(calc, number):
    calc.add(number)

@then(parsers.parse("the result should be {result}"))
def check_result(calc, result):
    assert calc.result == int(result)
