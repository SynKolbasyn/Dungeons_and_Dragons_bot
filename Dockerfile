FROM python:latest

LABEL authors="Andrew Kozmin"

RUN python3 -m pip install -U pip && \
    pip install "psycopg[binary]" && \
    pip install aiogram

WORKDIR /usr/src/dungeons_and_dragons_bot/

CMD ["python3", "src/main.py"]
