FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


RUN pip install pytest requests

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
