from transformers import pipeline

pipe =  pipeline("text-generation")


result  = pipe("Hello Students. Today we are going to learn about AI for humans", max_length=250, num_return_sequences=1)

print("Text Generation Results:")
for i, res in enumerate(result, start=1):
    print(f"Input {i}: {res['generated_text']}")