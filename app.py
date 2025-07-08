from flask import Flask, request, jsonify
import google.generativeai as genai
from flask_cors import CORS
import os


app = Flask(__name__)
CORS(app) 

#Gemini API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

# Initialize the Gemini model
model = genai.GenerativeModel("gemini-2.0-flash")



@app.route("/")
def home():
    return "Chatbot is running!."

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message")

    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    try:
        # Send the user message to Gemini AI
        response = model.generate_content(user_message)


        return jsonify({
            "user": user_message,
            "bot": response.text
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0", port=5000)