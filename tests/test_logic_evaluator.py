import pytest

from src.logic_evaluator import evaluate_expression


@pytest.mark.parametrize(
    "expected_bool,expression",
    [
        (True, {"==": [1, 1]}),
        (True, {"&&": [{"==": ["a", "a"]}, {"!": {"==": [1, 2]}}]}),
        (False, {"==": [True, False]}),
    ],
)
def test_evaluate_expression(expected_bool, expression):
    result = evaluate_expression(expression)
    assert result is expected_bool


def test_evaluate_expression_wrong():
    expression = {"!=": [1, 1]}
    with pytest.raises(Exception):
        evaluate_expression(expression)