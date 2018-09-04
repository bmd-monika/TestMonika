FROM python:3.6.2

WORKDIR /usr/app
COPY requirements.txt ./


RUN pip install -r requirements.txt
COPY ./ ./

CMD ["sh", "-c", "python manage.py runserver 0:8080"]
