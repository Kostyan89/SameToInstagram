FROM python:3.10

WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py .
COPY data data
COPY static static
COPY functions.py functions.py
COPY templates templates

CMD python app.py
