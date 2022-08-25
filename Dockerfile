FROM python:3.10

RUN apt update || apt upgrade || apk add bash

RUN mkdir /test_alsodev

WORKDIR /test_alsodev

COPY ./src ./
COPY ./commands ./commands
COPY ./requirements.txt ./requirements.txt

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["bash"]