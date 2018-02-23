FROM python:3.6
MAINTAINER Konstantinos Livieratos <kostas@intelligems.eu>

# Make sure all logs are correctly printed
ENV PYTHONUNBUFFERED=1

# Prepare source code directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Update setuptools
RUN pip install -U setuptools

# Install dependencies first, for better caching
COPY requirements.txt /usr/src/app/
RUN pip install -r requirements.txt
COPY ./ /usr/src/app/