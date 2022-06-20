# syntax=docker/dockerfile:1

FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir -p /backend-app

WORKDIR /backend-app
COPY ./backend /backend-app
COPY requirements.txt /backend-app

RUN pip install -r requirements.txt

COPY ./compose/backend/entry.sh /entry.sh
RUN chmod +x /entry.sh
ENTRYPOINT ["/entry.sh"]
