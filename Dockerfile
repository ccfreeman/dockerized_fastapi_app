FROM tiangolo/uvicorn-gunicorn:python3.8

RUN mkdir -p /engines

ADD app.py /
ADD engines/*.py /engines/

COPY requirements.txt .
COPY entry-point.sh .

WORKDIR /
RUN pip install -r requirements.txt

RUN chmod +x entry-point.sh

USER app_user
CMD ./entry-point.sh