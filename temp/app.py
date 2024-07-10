from flask import Flask, request, jsonify
from transformers import T5ForConditionalGeneration, T5Tokenizer

app = Flask(__name__)

# Replace with your actual Hugging Face access token (store securely)
model_name = "google/flan-t5-base"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

def predict_mood(feelings):
  input_ids = tokenizer(f"What is the mood of: {feelings}", return_tensors="pt")["input_ids"]
  output = model.generate(input_ids)
  predicted_mood = tokenizer.decode(output[0], skip_special_tokens=True)
  return predicted_mood

@app.route('/predict', methods=['POST'])
def predict():
  data = request.get_json()
  feelings = data.get('feelings')
  if not feelings:
    return jsonify({'error': 'Missing feelings data'}), 400

  prediction = predict_mood(feelings)
  return jsonify({'prediction': prediction})

if __name__ == '__main__':
  app.run(debug=True)
