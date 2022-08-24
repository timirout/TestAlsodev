FROM python:3.10

RUN apt update || apt upgrade || apk add bash

RUN mkdir /test_alsodev

WORKDIR /test_alsodev

COPY ./commands ./commands
COPY ./test_alsodev ./test_alsodev
COPY ./manage.py ./manage.py
COPY ./requirements.txt ./requirements.txt

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["bash"]