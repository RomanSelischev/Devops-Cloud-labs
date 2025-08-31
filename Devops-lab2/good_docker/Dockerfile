# Хороший

FROM python:3.13-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /good_docker
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

USER nobody
CMD ["python", "app.py"]
