FROM python:3.9-slim

RUN apt-get update && apt-get install -y iputils-ping net-tools && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY network_test.py /app

CMD ["python", "network_test.py"]
