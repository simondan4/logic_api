LOGIC_AND_OR_OPERATOR = {"&&": all, "||": any}


def evaluate_expression(expression: dict) -> bool:
    """Evaluates a logical expression from a dictionary.

    Args:
        expression (dict[str]): Logic expression

    Raises:
        Exception: If the user provides invalid logic operators

    Returns:
        (bool): Boolean for the evaluated expression
    """
    for bool_exp, values in expression.items():
        if bool_exp == "==":
            return values[0] == values[1]
        elif bool_exp == "!":
            logic_exp = evaluate_expression(values)
            return not logic_exp
        elif bool_exp in LOGIC_AND_OR_OPERATOR.keys():
            logic_operator = LOGIC_AND_OR_OPERATOR[bool_exp]
            logics = []
            for logic in values:
                logic_exp = evaluate_expression(logic)
                logics.append(logic_exp)
            return logic_operator(logics)
        else:
            raise Exception(
                f"{bool_exp} is not a valid logic operator. Should be any of '&&', '||', '!' or '=='"
            )
