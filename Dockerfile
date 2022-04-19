FROM python:3.8.3-alpine3.12

ENV PYTHONUNBUFFERED 1

RUN mkdir/Portal

WORKDIR /Portal

COPY . /Portal

RUN pip install  -r requirements.txt

CMD [ "gunicorn", "-c", "config/unicorn/conf.py", "--bind", ":8000","--chdir","Portal","portal.wsgi:application" ]

