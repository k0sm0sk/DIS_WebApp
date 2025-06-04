# We build on top of an existing python image
FROM python:3.13.1

# This image comes with a /code folder where we should have our code
WORKDIR /src

# Install required system libraries
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    musl-dev \
    postgresql \
    postgresql-contrib \
    libpq-dev \
    bash && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# For now we only copy pyproject.toml file to the docker image because we want to install all our Python libraries at this stage
COPY pyproject.toml pyproject.toml
RUN pip install -e .

EXPOSE 8080

# The entry point is called only when the container starts
ENTRYPOINT ["./entrypoint.sh"]