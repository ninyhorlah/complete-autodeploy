FROM python:3-alpine3.16

ENV PYTHONUNBUFFERED 1

WORKDIR /server

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "manage.py", "runserver" ]