from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class InputData(BaseModel):
    input: str

@app.post("/process")
async def process_input(data: InputData):
    user_input = data.input.lower()

    # Simple response logic
    if "hello" in user_input:
        reply = "Hello! I'm AGNI. How can I help you today?"
    elif "your name" in user_input:
        reply = "My name is AGNI – Advance General Network Intelligence."
    elif "who made you" in user_input:
        reply = "I was created by Anand with the help of ChatGPT!"
    else:
        reply = f"You said: {data.input}. I'm still learning to respond better."

    return {"output": reply}
