Feature: Calculator
    Scenario: Addition
        Given the calculator is cleared
        When I add 5
        Then the result should be 5

    Scenario: Addition 2
        Given the calculator is cleared
        When I add 5
        And I add 3
        Then the result should be 8
