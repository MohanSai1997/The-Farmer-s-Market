FROM python:3.7
WORKDIR /code
COPY src/ .
CMD [ "python", "./main.py"]