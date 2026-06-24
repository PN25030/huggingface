from transformers import pipeline

pipe = pipeline("sentiment-analysis")

results = pipe(["I love this product!", "the plastic quality is bad but I love this product!"])

print("Sentiment Analysis Results:")
for i, result in enumerate(results, start=1):   
    print(f"Input {i}: label={result['label']} score={result['score']:.4f}")