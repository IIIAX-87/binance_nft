# pull official base image
FROM python:3.9

# set work directory
WORKDIR /usr/src/

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY ./requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt


# copy project
COPY . .