FROM python:3.8
RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install -y build-essential

RUN groupadd -g 999 app_user && useradd -r -u 999 -g app_user app_user

RUN mkdir -p /app
# RUN mkdir -p /app/coyote

ADD src/*.py /app/
# ADD src/coyote/*.py /app/coyote/

COPY requirements.txt /app
COPY entry-point.sh /app

WORKDIR /app
RUN pip install -r requirements.txt

RUN chmod 755 entry-point.sh

USER app_user
CMD ["uvicorn", "main:app"]
# CMD ./entry-point.sh