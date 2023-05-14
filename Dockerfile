FROM tiangolo/uvicorn-gunicorn-starlette:python3.8
RUN pip freeze > requirements.txt
RUN pip install -r ./requirements.txt
COPY ./app /app