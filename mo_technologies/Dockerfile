FROM python:3

ENV PYTHONUNBUFFERED=1
ENV C_FORCE_ROOT=1
ENV DJANGODIR=/mo_technologies

RUN mkdir $DJANGODIR
WORKDIR $DJANGODIR

RUN pip3 install django
RUN pip3 install djangorestframework
RUN pip3 install django-model-utils
RUN pip3 install requests

COPY . $DJANGODIR/

RUN apt-get update && apt-get install -y gettext