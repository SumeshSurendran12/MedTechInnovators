# Start from a lightweight and up-to-date Python image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Install system-level dependencies (example: libs for matplotlib)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libfreetype6-dev \
    libpng-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file and install dependencies first (for build caching)
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the source code into the container
# Ensure src/ has an __init__.py to be recognized as a package
COPY src/ ./src/

# Set PYTHONPATH so Python can find src as a package without relative imports
ENV PYTHONPATH="/app:${PYTHONPATH}"

# If you want to run a specific script by default, set it here.
# For example, run generate_patient_data.py (adjust as needed):
CMD ["python", "src/generate_patient_data.py"]
