FROM python:3.8-slim

WORKDIR /app

COPY tp1.py .

RUN pip install requests
RUN pip install flask
RUN pip install uvicorn

CMD ["python","tp1.py"]