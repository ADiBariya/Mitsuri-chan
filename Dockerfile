FROM python:3.11-slim

# Install Node.js
RUN apt-get update && apt-get install -y nodejs npm

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the application code
COPY . .

# Expose the port
EXPOSE 8080

# Run the command to start the application
CMD ["python", "app.py"]
