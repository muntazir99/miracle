import openai

# Set up OpenAI API credentials
openai.api_key = "OPENAI_API_KEY"

def predict_mood(feeling):
    # Generate mood prediction using OpenAI's GPT-4 model
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"I am feeling {feeling}. generate a motivational quote for this."}
    ]
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7
    )
    mood_prediction = response.choices[0].message['content'].strip()

    return mood_prediction

# Get user input for their feeling
user_feeling = input("How are you feeling today? ")

# Predict the user's mood
def quote_return(user_feeling):
    predicted_mood = predict_mood(user_feeling)
    return predicted_mood


# print(f"{predicted_mood}")
