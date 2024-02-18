FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10-slim

COPY ./app /app/app

RUN pip install --no-cache-dir fastapi uvicorn

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]