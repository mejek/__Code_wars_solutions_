from evaluate_a_postfix_expression import postfix_evaluator
import pytest

input_expected = (
                ("2 3 +", 5),
                ("2 -3 +", -1),
                ("1", 1),
                ("-1", -1),
                ("2 3 9 4 / + *", 10),
                ("3 4 9 / *", 0),
                ("4 8 + 6 5 - * 3 2 - 2 2 + * /", 3),
                ("2 3 9 4 / + *", 10),
                ("3 4 9 / *", 0),
                ("4 8 + 6 5 - * 3 2 - 2 2 + * /", 3),
                ("21 21 +", 42),
                ("-42 42 +", 0),
        )

@pytest.mark.parametrize("test_input, expected", input_expected)
def test_pendulum(test_input, expected):
    assert postfix_evaluator(test_input) == expected

