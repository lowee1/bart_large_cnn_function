from python:3.11-slim

WORKDIR /

ADD requirements.txt .
RUN pip install -r requirements.txt

ADD summarize.py .

CMD python /summarize.py
