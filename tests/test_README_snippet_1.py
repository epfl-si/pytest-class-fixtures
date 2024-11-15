from pytest_class_fixtures import class_fixture

@class_fixture(name="calc")
class Calculator:
    def __init__(self):
        self.result = 0

def test_calculator_initial_state(calc):
    assert calc.result == 0
