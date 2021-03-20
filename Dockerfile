FROM python:3.8
RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install -y build-essential
# RUN apt-get update && apt-get install -y build-essential 
    # && rm -rf /var/lib/apt/lists/*

RUN groupadd -g 999 app_user && useradd -r -u 999 -g app_user app_user

RUN mkdir -p /src
RUN mkdir -p /src/engines

ADD src/*.py /src/
ADD src/engines/*.py /src/engines/

COPY requirements.txt .
COPY entry-point.sh .

# WORKDIR .
RUN pip install -r requirements.txt

RUN chmod 755 entry-point.sh

USER app_user
# CMD ["python", "main.py"]
# CMD ["uvicorn", "src:app"]
CMD ./entry-point.sh
