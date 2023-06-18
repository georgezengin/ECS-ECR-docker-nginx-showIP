# Base image with Python
FROM python:3.10-alpine

WORKDIR /app
COPY IPshow.py .
COPY requirements.txt .

# Install Python libraries
RUN pip install --no-cache-dir -r requirements.txt

# Run the Python script
ENV FLASK_APP="IPshow.py"
EXPOSE 80
#CMD ["python", "IPshow.py"]
CMD flask run --port=80 --host=0.0.0.0
