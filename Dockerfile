FROM python:3

WORKDIR /usr/src/app

COPY ./titanic /app
WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "gunicorn", "--workers=2", "-b 0.0.0.0:80", "main:app" ]
