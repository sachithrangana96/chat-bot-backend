#  Gemini Chatbot API (Flask + Docker)

This is a simple, Dockerized chatbot REST API built with **Flask** and powered by **Google Gemini (Generative AI)**. It allows users to send messages and receive AI-generated responses.

---

##  Features

-  Chatbot using Gemini API
-  Secure API key via `.env` file
-  Docker support for easy deployment
-  CORS enabled for frontend integration
-  Simple REST endpoint `/api/chat`

---

##  Prerequisites

- Python 3.11+ (for local development)
- Docker & Docker Compose (for containerized use)
- Gemini API Key (Get one from [Google AI Studio](https://makersuite.google.com/))

---

##  Local Development Setup

###  Clone the repo

git clone [https://github.com/your-username/chatbot.git](https://github.com/sachithrangana96/chat-bot-backend.git)
cd chat-bot-backend

###  Create env file
Then add your Gemini API key inside .env

GEMINI_API_KEY=your_real_gemini_api_key_here

###  Install python depencies and Run

pip install -r requirements.txt
python app.py



