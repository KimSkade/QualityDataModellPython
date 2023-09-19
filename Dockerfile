ARG APP_VERSION=0.1.1

FROM python:3.11-slim

WORKDIR /dependencies

RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the poetry files into the container
COPY ba-syx-aas-repository-client/ /app/ba-syx-aas-repository-client
COPY ba-syx-submodel-repository-client/ /app/ba-syx-submodel-repository-client
COPY pyproject.toml poetry.lock /app/

# Install dependencies using Poetry
RUN pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi \
    && pip install git+https://github.com/sdm4fzi/aas2openapi.git@main

COPY . /app

EXPOSE 8000

CMD ["python", "einfacherTestToServer.py"]