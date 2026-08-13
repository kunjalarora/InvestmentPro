# Adjust base image / entrypoint / port to match your actual app
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

# Change this to however your app actually starts
# e.g. gunicorn, uvicorn, python app.py, etc.
CMD ["python", "app.py"]
