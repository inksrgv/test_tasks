FROM python:3.9-slim
WORKDIR /yadro-test-task
COPY file.txt script.py ./
RUN chmod +x script.py
ENTRYPOINT ["python3", "script.py", "file.txt"]


