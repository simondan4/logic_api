from asyncio import FastChildWatcher
import pytest
from fastapi.testclient import TestClient
from src.main import app


@pytest.mark.parametrize(
    "expected_bool,expression",
    [
        (True, {"==": [1, 1]}),
        (True, {"&&": [{"==": ["a", "a"]}, {"!": {"==": [1, 2]}}]}),
        (False, {"==": [True, False]}),
    ],
)
def test_app_evaluate(expected_bool, expression):
    client = TestClient(app)
    response = client.post("/evaluate", json=expression)
    response_result = response.json()
    assert expected_bool is response_result