from python:3.11-slim

WORKDIR /

RUN pip install transformers
RUN pip install runpod

ADD summarize.py .

CMD python /summarize.py
