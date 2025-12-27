A full-stack web application that analyzes short bios and classifies them into green, yellow, and red flags, with an optional AI-generated rewritten version of the bio.
The system is built with a React frontend and a FastAPI backend, using structured NLP analysis and an external LLM for text rewriting.

Overview
The application accepts a short bio as input and returns:
Detected positive, risky, and negative language signals
Confidence scores for each category
An optional rewritten version of the bio with a selected tone
The frontend is responsible only for user interaction and displaying results.
All analysis and rewriting logic is handled by the backend.

API Endpoints
POST /classify

Request:
{
  "bio": "I am serious about my career. Don’t waste my time."
}

Response:
{
  "green_flags": ["confident"],
  "yellow_flags": [],
  "red_flags": ["dismissive"],
  "scores": {
    "confident": 0.61,
    "dismissive": 0.72
  }
}

POST /rewrite

Request:
{
  "bio": "I am serious about my career. Don’t waste my time.",
  "tone": "confident"
}

Response:
{
  "improved_bio": "I’m focused on my career and value meaningful conversations with people who share that mindset."
}

Environment Variables
Backend
Create a .env file in the backend directory:
GEMINI_API_KEY=your_api_key_here

Running Locally
Backend
cd backend
pip install -r requirements.txt
python -m uvicorn app:app --reload

Frontend
cd frontend
npm install
npm run dev
