# pull official base image
FROM python:3.12-alpine

# set work directory
WORKDIR /opt/python-projects/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN set -eux \
    && apk add --no-cache --virtual .build-deps build-base \
        gcc python3-dev \
    && pip install --upgrade pip setuptools wheel \
    && rm -rf /root/.cache/pip

# copy requirements file
COPY ./requirements.txt /opt/python-projects/app/requirements.txt

RUN pip install --upgrade pip
RUN pip install -r /opt/python-projects/app/requirements.txt


# copy project
COPY . /opt/python-projects/app/
# RUN ls -la
# RUN PYTHONPATH=. alembic upgrade head
