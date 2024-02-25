FROM python:latest

LABEL authors="Andrew Kozmin"

ADD requirements.txt /tmp/

RUN python3 -m pip install -U pip setuptools wheel && \
    pip install -r /tmp/requirements.txt

WORKDIR /usr/src/dungeons_and_dragons_bot/

CMD ["python3", "src/main.py"]
