# Dockerfile for backend (FastAPI / Uvicorn)
# Builds the app from the backend/ directory. Adjust APP_MODULE if your ASGI app module differs.

FROM python:3.11-slim

WORKDIR /app
ENV PYTHONUNBUFFERED=1

# Install system deps if you need to compile any wheels (uncomment if necessary)
# RUN apt-get update && apt-get install -y build-essential gcc libpq-dev && rm -rf /var/lib/apt/lists/*

COPY backend/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY backend/ /app/backend

# Set the ASGI application module: change if your app module differs.
# Example: backend.main:app
ENV APP_MODULE=backend.main:app

EXPOSE 8000

# Use shell form so environment variable expansion works for APP_MODULE
ENTRYPOINT ["sh", "-c"]
CMD ["uvicorn ${APP_MODULE} --host 0.0.0.0 --port 8000"]
