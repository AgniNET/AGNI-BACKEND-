# main.py
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow CORS (for frontend apps to connect)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development, use specific origin in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Predefined responses (can be expanded)
predefined_responses = {
    "hello": "Hello! How can I help you today?",
    "hi": "Hi there!",
    "bye": "Goodbye! Have a nice day!",
    "what is your name": "I am a simple chatbot created using FastAPI.",
    "how are you": "I'm just code, but I'm functioning perfectly!"
}

@app.post("/chat")
async def chat(req: Request):
    data = await req.json()
    user_input = data.get("message", "").lower().strip()

    # Find response
    response = predefined_responses.get(user_input, "Sorry, I didn't understand that.")

    return {"response": response}
