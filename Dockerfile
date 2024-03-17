# Use Python Alpine as base image
FROM python:alpine

# Set working directory
WORKDIR /app

# Prepare necessary files
COPY games/ /app/games/
COPY templates/ /app/templates/
COPY *.py /app/
COPY requirements.txt .
RUN echo "2" > /app/Scores.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run Flask app with gunicorn in the foreground
CMD ["gunicorn", "--bind", "0.0.0.0:20000", "main_score:app"]
