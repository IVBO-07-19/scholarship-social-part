FROM python:3

RUN mkdir -p /usr/src/social/
WORKDIR /usr/src/social
COPY . .

RUN pip install -r requirements.txt