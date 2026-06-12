# A Docker image starts from another image.
# This one gives us Python without extra tools we do not need.
FROM python:3.12-slim

# Everything after this will happen inside /app in the container.
WORKDIR /app

# These settings make Python logs easier to see in Docker.
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install Python packages first so Docker can cache this step.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project into the container.
COPY . .

# Flask will run inside the container on port 5000.
EXPOSE 5000

# Start the Flask app. The host must be 0.0.0.0 so your browser can reach it.
CMD ["flask", "--app", "app:create_app", "run", "--host=0.0.0.0", "--port=5000"]
