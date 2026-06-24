from transformers import pipeline

pipe = pipeline("text-classification", model="google/tapas-small-finetuned-tabfact")

results = pipe(["This restaurant is awesome", "This restaurant is awful"])

def interpret_score(score):
    if score >= 0.9:
        return "very confident"
    if score >= 0.75:
        return "confident"
    if score >= 0.5:
        return "somewhat confident"
    return "low confidence"

for i, result in enumerate(results, start=1):
    confidence = interpret_score(result["score"])
    print(f"Input {i}: label={result['label']} score={result['score']:.4f} ({confidence})")