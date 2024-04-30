FROM python:3.10-alpine
COPY . /app
RUN apk add libpq-dev gcc libc-dev
RUN pip install -r /app/requirements.txt
CMD ["python","/app/run.py"]