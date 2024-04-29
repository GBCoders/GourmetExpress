FROM python:3.10-alpine
RUN pip install flask
COPY . /app
# COPY . /database /docker-entrypoint.initdb.d/
CMD ["python","/app/run.py"]