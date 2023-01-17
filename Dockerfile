ARG PYTHON_BASE=python:3.10.8-slim-bullseye
FROM ${PYTHON_BASE}

WORKDIR /app


COPY Pipfile.lock Pipfile ./
COPY src/ ./src

RUN apt-get update -y && \
    pip install --upgrade pip && \
    pip install pipenv && \
    pipenv sync --system

ENTRYPOINT ["uvicorn", "src.main:app"]
CMD ["--host", "0.0.0.0", "--port", "80"]