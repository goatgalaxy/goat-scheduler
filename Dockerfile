# Image
FROM python:3.8.5-slim-buster

# Install pipenv
RUN pip install pipenv

# Env vars
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive

# Workdir
WORKDIR /app

# Install dependencies
COPY Pipfile Pipfile.lock /app/
RUN pipenv install --system --deploy

# Copy project
ADD . /app/

# Run
CMD python -m scheduler 
