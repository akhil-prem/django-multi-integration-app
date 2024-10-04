FROM python:3.8.5-alpine

# Install build dependencies
RUN apk add --no-cache build-base

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY . .

# Run migrations
RUN python manage.py migrate
