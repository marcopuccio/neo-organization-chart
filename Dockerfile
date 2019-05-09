FROM python:3.6.8-slim-stretch
ENV PYTHONUNBUFFERED 1

# Copy source to app dir
RUN mkdir /app
COPY ["organization/", "Pipfile", "Pipfile.lock", "/app/"]
WORKDIR /app

# Install deps and remove apt lists
RUN apt-get update \
  && apt-get upgrade -y \
  && apt-get install --no-install-recommends -y \
    build-essential \
    python3-dev \
  && pip install --upgrade pip \
  && pip install pipenv \
  && pipenv install --system --deploy \
  && apt-get autoremove -y \
  && apt-get clean && rm -rf /var/lib/apt/lists/*
