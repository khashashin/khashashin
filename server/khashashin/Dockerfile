# pull official base image
FROM python:3.8.3-alpine
LABEL maintainer="khashashin"

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE khashashin.settings.prod

ENV PATH="/scripts:${PATH}"

RUN mkdir /app
RUN mkdir /app/staticfiles
RUN mkdir /app/media
RUN mkdir /scripts
WORKDIR /app

RUN apk add --update --no-cache --virtual .tmp libc-dev linux-headers
RUN apk add jpeg-dev zlib-dev postgresql-dev gcc python3-dev musl-dev
ENV LIBRARY_PATH=/lib:/usr/lib

# Install dependencies
RUN pip install --upgrade pip
COPY Pipfile* /app/
RUN pip install pipenv
RUN pipenv install --system --skip-lock
RUN apk del .tmp

# Copy project
COPY . /app
COPY ./scripts /scripts
RUN chmod +x /scripts/*

RUN addgroup -S khas && adduser -S khas -G khas
RUN chown -R khas:khas /app/*
RUN chmod -R 755 /app/*
USER khas

# run entrypoint.sh
ENTRYPOINT ["entrypoint.sh"]
