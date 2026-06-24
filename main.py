from transformers import pipeline

pipe = pipeline("text-classification", model="google/flan-t5-large")

pipe(["This restaurant is awesome", "This restaurant is awful"])
