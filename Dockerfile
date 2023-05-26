# Use the official Python base image
FROM python:3.8-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install the dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the container
COPY . .

# Expose the port on which the Flask application will run
EXPOSE 5000

# Set the environment variables
ENV FLASK_APP=app.py
#ENV FLASK_RUN_HOST=0.0.0.0

# Run the Flask application
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0" ]

