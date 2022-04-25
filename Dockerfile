FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY ./requirements.txt /app/
WORKDIR /app/
RUN python -m pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./app /app/app

ENV APP_MODULE=app.main:app