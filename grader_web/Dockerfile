FROM python:3

EXPOSE 8000
EXPOSE 11112

WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

RUN python manage.py migrate

CMD python manage.py runserver 0.0.0.0:8000
