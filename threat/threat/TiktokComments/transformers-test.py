from transformers import pipeline

classifier = pipeline("sentiment-analysis")

res = classifier("waiting for this course my whole life")

print(res)