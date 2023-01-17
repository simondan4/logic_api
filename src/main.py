import json
import os
from typing import Dict

from fastapi import FastAPI, Request

from .logic_evaluator import evaluate_expression

app = FastAPI(title="Logic Evaluator")


@app.post("/evaluate")
async def evaluate(request: Request) -> bool:
    """Creates a prediction based on an API request.

    Args:
        request (Request): Request with logic expression.

    Returns:
        (bool): Result of evaluated expression
    """
    logic_request = await request.json()

    response = evaluate_expression(logic_request)

    return response
