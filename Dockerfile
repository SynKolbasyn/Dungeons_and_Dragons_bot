FROM python:latest

LABEL authors="Andrew Kozmin"

RUN python3 -m pip install -U pip && \
    pip install "psycopg[binary]"

CMD ["tail", "-f", "/dev/null"]
