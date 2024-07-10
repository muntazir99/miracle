const { OpenAIApi } = require("openai");
const readline = require("readline");

// Set up OpenAI API configuration
const openai = new OpenAIApi({
  apiKey: 'your_openai_api_key_here'  // Replace with your OpenAI API key
});

// Set up readline interface for user input
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function askQuestion(query) {
  return new Promise(resolve => rl.question(query, resolve));
}

async function getMood(feelings) {
  const prompt = `The user described their feelings as: "${feelings}". Based on these feelings, predict the user's mood.`;

  const response = await openai.createCompletion({
    model: "text-davinci-003",  // Use the appropriate model
    prompt: prompt,
    max_tokens: 50,
    temperature: 0.7,
  });

  const moodPrediction = response.data.choices[0].text.trim();
  return moodPrediction;
}

(async () => {
  console.log("Hello! I can help you predict your mood based on your feelings.");
  const feelings = await askQuestion("Please enter your feelings: ");
  
  const mood = await getMood(feelings);
  console.log(`Based on your feelings, your predicted mood is: ${mood}`);
  
  rl.close();
})();
