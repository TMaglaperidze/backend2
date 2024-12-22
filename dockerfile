FROM python:3.12-slim

COPY  backend.py .

RUN pip install flask requests

EXPOSE 5002
CMD ["python", "backend.py"]
