FROM python:3.14.0a3-slim
WORKDIR /app
ADD . /app
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT ["/app/entrypoint.sh"]
