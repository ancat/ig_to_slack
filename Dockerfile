FROM python:3.9-slim-bullseye
RUN apt update
RUN apt install -y git
RUN python3 -m venv /opt/venv
COPY requirements.txt .
RUN /opt/venv/bin/pip install -r requirements.txt
COPY patched_extractors.py /opt/venv/lib/python3.9/site-packages/instagrapi/extractors.py
COPY src /opt/notifier
CMD ["/opt/venv/bin/python", "/opt/notifier/main.py"]
