# forecast + ingestion microservice
FROM python:3.9-slim

# System dependencies for Prophet
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    build-essential \
    libpython3-dev \
    curl \
    libatlas-base-dev \
    libprotobuf-dev \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Install required python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy code
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Start FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
