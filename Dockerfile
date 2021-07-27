FROM python:3.8

LABEL mantainer="Taurai Valentine Maputsa"

COPY . /app

WORKDIR /app 

RUN pip install -r requirements.txt

CMD ["python", "api.py"]