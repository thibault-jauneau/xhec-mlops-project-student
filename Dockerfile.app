FROM python:3.10.14-slim

WORKDIR /app_home

COPY ./requirements.txt /app_home/requirements.txt

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r /app_home/requirements.txt

COPY ./src /app_home/src

COPY ./data /app_home/data

COPY ./bin/run_services.sh /app_home/src/web_service/run_services.sh

WORKDIR /app_home/src/web_service

EXPOSE 8001

EXPOSE 5000

EXPOSE 4201

CMD ["bash", "run_services.sh"]
