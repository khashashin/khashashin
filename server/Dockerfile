# pull official base image
FROM python:3.8-slim-buster

RUN apt-get update \
    && apt-get install -y build-essential \
    && apt-get install -y libpq-dev \
    && apt-get install -y gettext \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir /app
RUN mkdir /app/staticfiles
RUN mkdir /app/media
RUN mkdir /scripts
WORKDIR /app

# RUN apk add --update --no-cache --virtual .tmp libc-dev linux-headers
# RUN apk add jpeg-dev zlib-dev postgresql-dev gcc python3-dev musl-dev make

# Install dependencies
RUN pip install --upgrade pip
COPY Pipfile* /app/
RUN pip install pipenv
RUN pipenv install --system --skip-lock
# RUN apk del .tmp

# Copy project
COPY . /app
COPY ./scripts /scripts
RUN sed -i 's/\r$//g' /scripts/entrypoint.sh
RUN chmod +x /scripts/*

RUN addgroup --system khas && adduser --system --ingroup khas khas
RUN chown khas:khas /app/*
RUN chown khas:khas /scripts/*
RUN chmod 755 /app/*
USER khas

# run entrypoint.sh
ENTRYPOINT ["sh", "/scripts/entrypoint.sh"]
