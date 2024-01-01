from transformers import pipeline
import runpod
import torch

print(torch.cuda.is_available(), flush=True)

device = 0 if torch.cuda.is_available() else -1
summarizer = pipeline("summarization", model="facebook/bart-large-cnn", device=device)


def summarize(job):
    job_input = job["input"]
    text = job_input["text"]

    summary = summarizer(text, min_length=5, max_length=100)[0]["summary_text"]
    return summary


runpod.serverless.start({"handler": summarize})
