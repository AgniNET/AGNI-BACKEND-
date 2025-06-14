from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# CORS setup for frontend-backend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can replace "*" with your frontend URL for better security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Input format expected from frontend
class InputData(BaseModel):
    input: str

# Process route to handle input and return output
@app.post("/process")
async def process_input(data: InputData):
    user_input = data.input

    # ⚙️ Temporary simple logic: Echo the input
    response = f"AGNI Response: {user_input}"

    # In future: Add real processing logic here
    return {"output": response}
