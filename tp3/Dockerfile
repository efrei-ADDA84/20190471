FROM python:3.8-slim

WORKDIR /app

COPY tp3.py .

RUN pip install requests
RUN pip install flask
RUN pip install uvicorn

CMD ["python","tp3.py"]