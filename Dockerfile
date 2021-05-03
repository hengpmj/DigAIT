# pull official base image
FROM python:3.7

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# run gunicorn
CMD gunicorn portfolio.wsgi:application --bind 0.0.0.0:$PORT
