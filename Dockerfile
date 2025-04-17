FROM python:3.10-slim

WORKDIR /app

RUN pip install --no-cache-dir \
    opentelemetry-api \
    opentelemetry-sdk \
    opentelemetry-exporter-otlp \
    opentelemetry-semantic-conventions

COPY app.py .

CMD ["python", "app.py"]