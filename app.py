import openai
from flask import Flask, request, render_template
from dotenv import load_dotenv
import os

# Load OpenAI API key from .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

def chat_with_gpt(prompt):
    """Send user prompt to OpenAI and return the response."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Switch to "gpt-4" for better results
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

@app.route("/", methods=["GET", "POST"])
def home():
    """Handle homepage with chat form."""
    bot_response = None
    if request.method == "POST":
        user_input = request.form.get("user_input")
        bot_response = chat_with_gpt(user_input)
    return render_template("index.html", bot_response=bot_response)

if __name__ == "__main__":
    app.run(debug=True)  # Run locally
