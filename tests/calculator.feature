Feature: Calculator
    Scenario: Addition
        Given the calculator is cleared
        When I add 5
        Then the result should be 5
