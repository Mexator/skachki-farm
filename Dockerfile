FROM ubuntu:latest
RUN set -ex; \
    apt-get update; \
    apt-get install -y --no-install-recommends \
        python3 python3-pip; \
    pip3 install --upgrade setuptools; \
    pip3 install wheel telethon; \
    rm -rf /var/lib/apt/lists/*
COPY main.py .
COPY skacki_farm.session .
CMD ["python3","main.py"]
