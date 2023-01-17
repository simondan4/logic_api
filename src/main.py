import json
import os
from typing import Dict

from fastapi import FastAPI, Request

from .logic_evaluator import evaluate_expression

# LOGIC_AND_OR_OPERATOR = {"&&": all, "||": any}

# LOGIC_AND_OR = {"&&": "and", "||": "or"}


# def format_expression(expression):
#     for bool_exp, values in expression.items():
#         if bool_exp == "==":
#             return f"('{values[0]}' == '{values[1]}')"
#         elif bool_exp == "!":
#             logic_exp = format_expression(values)
#             return f"not {logic_exp}"
#         elif bool_exp in LOGIC_AND_OR.keys():
#             logic_bool = LOGIC_AND_OR[bool_exp]
#             logics = []
#             for logic in values:
#                 logic_exp = format_expression(logic)
#                 logics.append(logic_exp)
#             logic_bool_comb = f" {logic_bool} ".join(logics)
#             return f"({logic_bool_comb})"
#         else:
#             raise Exception(
#                 f"{bool_exp} is not a valid logic operator. Should be any of '&&', '||', '!' or '=='"
#             )


app = FastAPI(title="Logic Evaluator")


@app.post("/evaluate")
async def evaluate(request: Request) -> bool:
    """Creates a prediction based on an API request.

    Args:
        request (Request): Request with logic expression.

    Returns:
        (bool): Result of evaluated expression
    """
    try:
        logic_request = await request.json()

        response = evaluate_expression(logic_request)
    except Exception as error:
        response = {"error": f"{error} having request: {json.dumps(request)}"}

    finally:
        return response
