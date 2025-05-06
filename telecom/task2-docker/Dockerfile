FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y --no-install-recommends python3 python3-pip && \
    rm -rf /var/lib/apt/lists/* && \
    pip install requests

WORKDIR /os

COPY script.py ./

CMD ["python3", "script.py"]