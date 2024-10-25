# Step 1: Use the official Python image from Docker Hub
FROM python:3.11-alpine

# Step 2: Set the working directory
WORKDIR /app

# Step 3: Install PostgreSQL client and build dependencies
RUN apk update && apk add --no-cache \
    gcc \
    musl-dev \
    postgresql-dev \
    libpq

# Step 4: Copy the current directory contents into the container at /app
COPY . .

# Step 5: Install Python dependencies (including psycopg2)
RUN pip install --no-cache-dir -r requirements.txt

# Step 6: Expose port 5000 for the Flask app
EXPOSE 5000

# Step 7: Set environment variables and start Flask app
ENV FLASK_APP=app.py
CMD ["flask", "run", "--host=0.0.0.0"]
