FROM python:3.11-slim

WORKDIR /app3

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app3.py"]
