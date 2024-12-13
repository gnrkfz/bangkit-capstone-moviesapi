FROM python:3.12

WORKDIR /app

ENV HOST 0.0.0.0

COPY . .

RUN pip install --no-cache-dir fastapi==0.111.0 uvicorn==0.30.1 pandas==2.2.2 requests==2.32.3

EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
