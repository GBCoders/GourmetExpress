FROM python:3.10-alpine
RUN pip install flask
COPY . /app
CMD ["python","/app/run.py"]
