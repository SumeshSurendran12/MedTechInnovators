# Start from a lightweight Python base image
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Install system-level dependencies if needed (example: lib for matplotlib)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libfreetype6-dev \
    libpng-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code into the container
COPY src/ ./src/

# Expose a port if your app runs a server (optional)
# EXPOSE 8080

# By default, just run a simple command (e.g., show help or run a script)
CMD ["python", "-c", "print('Container is ready. Run desired scripts with docker run ...')"]
