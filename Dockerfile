FROM docker.arvancloud.ir/python:3.12.4-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /src

COPY requirements.txt .  
RUN pip install --upgrade pip \
    && pip install --retries 10 -r requirements.txt

COPY . .  

CMD ["python", "main.py"]
