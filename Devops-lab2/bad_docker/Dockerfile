# Плохой

FROM python:3.7

RUN apt-get update
RUN apt-get install -y git
RUN apt-get install -y curl

WORKDIR /bad_docker

ADD . .

RUN pip install --no-cache-dir -r requirements.txt
RUN echo "SECRET_TOKEN=12345" >> /bad_docker/.env

CMD ["python", "app.py"]
