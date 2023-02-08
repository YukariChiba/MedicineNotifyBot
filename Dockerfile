FROM python:alpine
RUN mkdir /code
COPY . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["python", "main.py"]
