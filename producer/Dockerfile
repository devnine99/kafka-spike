FROM python:3.8.5
MAINTAINER devnine99@gmail.com

RUN mkdir /app
WORKDIR /app

ADD . /app/
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "main.py"]
