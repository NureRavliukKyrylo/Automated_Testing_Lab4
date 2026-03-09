import pytest
from pytest_bdd import given, when, then, scenarios, parsers

scenarios("../features/calculator.feature")

@given("I have a calculator")
def i_have_a_calculator(calc, context):
    context["calc"] = calc

@when(parsers.parse("I add {a:g} and {b:g}"))
def add_two_numbers(a, b, context):
    context["result"] = context["calc"].add(a, b)

@when(parsers.parse("I subtract {b:g} from {a:g}"))
def subtract_two_numbers(a, b, context):
    context["result"] = context["calc"].subtract(a, b)

@when(parsers.parse("I multiply {a:g} by {b:g}"))
def multiply_two_numbers(a, b, context):
    context["result"] = context["calc"].multiply(a, b)

@when(parsers.parse("I divide {a:g} by {b:g}"))
def divide_two_numbers(a, b, context):
    context["result"] = context["calc"].divide(a, b)

@then(parsers.parse("the result should be {expected:g}"))
def result_should_be(expected, context):
    assert context["result"] == pytest.approx(expected)

@when(parsers.parse("I multiply {a:d} by {b:d}"))
def multiply_large_numbers(a, b, context):
    context["result"] = context["calc"].multiply(a, b)

@then(parsers.parse("the result should be {expected:d}"))
def result_should_be_large(expected, context):
    assert context["result"] == expected

@when(parsers.parse("I attempt to divide {a:g} by {b:g}"))
def attempt_to_divide(a, b, context):
    context["a"] = a
    context["b"] = b
    context["operation"] = "divide"

@then(parsers.parse('a ValueError should be raised with message "{message}"'))
def value_error_raised(message, context):
    with pytest.raises(ValueError, match=message):
        calc = context["calc"]
        if context.get("operation") == "add":
            calc.add(context["a"], context["b"])
        else:
            calc.divide(context["a"], context["b"])

@when(parsers.parse('I attempt to add "{a}" and "{b}"'))
def attempt_invalid_add(a, b, context):
    context["a"] = a
    context["b"] = b
    context["operation"] = "add"