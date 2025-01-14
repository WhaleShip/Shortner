FROM python:3.11-slim

COPY ./ ./

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8090


CMD ["python", "main.py"]