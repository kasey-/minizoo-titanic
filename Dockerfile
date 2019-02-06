FROM python:3

COPY ./titanic /app
WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "gunicorn", "--workers=4", "-b 0.0.0.0:80", "main:app" ]
