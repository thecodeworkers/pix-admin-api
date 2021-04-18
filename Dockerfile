FROM python:3.8-alpine

WORKDIR /usr/app

RUN apk add gcc musl-dev python3-dev libffi-dev openssl-dev cargo
COPY requirements.txt /usr/app

RUN pip install -r requirements.txt
COPY . /usr/app

CMD ["flask", "run"]
