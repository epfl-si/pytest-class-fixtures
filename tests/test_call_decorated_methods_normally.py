from pytest_bdd import given, when, then, parsers, scenarios
from pytest_class_fixtures import class_fixture

@class_fixture(name="calc")
class Calculator:
    def __init__ (self):
        self.clear()

    @given("the calculator is cleared")
    def clear (self):
        self.result = 0

    @when(parsers.parse("I add {number}"))
    def add (self, number):
        self.result += int(number)

@then(parsers.parse("the result should be {result}"))
def check_result(calc, result):
    assert calc.result == int(result)

def test_it():
    calc = Calculator()
    assert calc.result == 0
    calc.add(1)
    calc.add(2)
    assert calc.result == 3


