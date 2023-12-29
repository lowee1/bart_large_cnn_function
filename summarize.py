from transformers import pipeline
import runpod

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")


def summarize(job):
    job_input = job["input"]
    text = job_input["text"]

    summary = summarizer(text, min_length=5, max_length=100)[0]["summary_text"]

    return summary


runpod.serverless.start({"handler": summarize})
