# Use the official Python 3.13.4 slim image as the base image
FROM python:3.13.4-slim-bullseye

# Create a non-root user
RUN groupadd -r appuser && useradd -r -g appuser appuser

RUN apt-get update && apt-get install -y curl

# Create Virtual environment
RUN python -m venv /opt/venv/

ENV PATH=/opt/venv/bin:$PATH

# Set the working directory inside the container to /app
WORKDIR /app

# Copy the requirements file to a temporary location in the container
COPY requirements.txt /tmp/requirements.txt

# Install Python dependencies from the requirements file
RUN pip install -r /tmp/requirements.txt

# Copy the application source code into the container
COPY ./src .

# Change ownership of the app directory to the non-root user
RUN chown -R appuser:appuser /app /opt/venv

# Switch to the non-root user
USER appuser

# Set the default command to run a simple HTTP server on port 8000
CMD ["python", "-m", "http.server", "8000"]