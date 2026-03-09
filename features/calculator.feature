Feature: Calculator Operations
  As a user of the calculator
  I want to perform arithmetic operations
  So that I can get accurate results

  Background:
    Given I have a calculator

  # ADD

  Scenario Outline: Add two numbers
    When I add <a> and <b>
    Then the result should be <result>

    Examples:
      | a    | b    | result |
      | 2    | 3    | 5      |
      | -2   | -3   | -5     |
      | -5   | 3    | -2     |
      | 0    | 5    | 5      |
      | 0    | 0    | 0      |
      | 2.5  | 3.5  | 6.0    |
      | 2    | 3.5  | 5.5    |

  # SUBTRACT

  Scenario Outline: Subtract two numbers
    When I subtract <b> from <a>
    Then the result should be <result>

    Examples:
      | a    | b    | result |
      | 5    | 3    | 2      |
      | -5   | -3   | -2     |
      | -5   | 3    | -8     |
      | 5    | 0    | 5      |
      | 0    | 5    | -5     |
      | 5.5  | 2.5  | 3.0    |

  # MULTIPLY

  Scenario Outline: Multiply two numbers
    When I multiply <a> by <b>
    Then the result should be <result>

    Examples:
      | a    | b   | result |
      | 4    | 3   | 12     |
      | -4   | 3   | -12    |
      | -4   | -3  | 12     |
      | 5    | 0   | 0      |
      | 0    | 5   | 0      |
      | 2.5  | 2   | 5.0    |

  # DIVIDE

  Scenario Outline: Divide two numbers
    When I divide <a> by <b>
    Then the result should be <result>

    Examples:
      | a    | b    | result |
      | 10   | 2    | 5      |
      | -10  | 2    | -5     |
      | -10  | -2   | 5      |
      | 0    | 5    | 0      |
      | 5.0  | 2.0  | 2.5    |

  # LARGE NUMBERS

  Scenario: Multiply large numbers
    When I multiply 10000000000 by 10000000000
    Then the result should be 100000000000000000000

  # EXCEPTIONS

  Scenario: Divide by zero raises an error
    When I attempt to divide 10 by 0
    Then a ValueError should be raised with message "Cannot divide by zero."

  Scenario Outline: Invalid types raise an error
    When I attempt to add "<a>" and "<b>"
    Then a ValueError should be raised with message "Inputs must be numbers"

    Examples:
      | a  | b  |
      | 2  | 3  |
      | 5  | 3  |
      | a  | b  |
      | 10 | 2  |