FROM tiangolo/uvicorn-gunicorn:python3.8

ADD requirements.txt /app

COPY ./app /app/app

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]