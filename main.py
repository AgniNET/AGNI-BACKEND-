from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class InputData(BaseModel):
    input: str

@app.get("/")
def root():
    return {"message": "Welcome to AGNI backend"}

@app.post("/process")
async def process(data: InputData):
    user_input = data.input.lower()

    # Simple intelligent response logic
    if "namaste" in user_input:
        response = "Namaste! Main AGNI hoon, aapki sahayata ke liye yahan hoon."
    elif "kaun ho" in user_input or "tum kaun ho" in user_input:
        response = "Main AGNI hoon – Advanced General Network Intelligence, ek AGI assistant."
    elif "kya kar sakte ho" in user_input:
        response = "Main text, image, video, audio analyze kar sakta hoon, aur ethical hacking, data synthesis, aur advanced AI tasks bhi."
    elif "shukriya" in user_input or "thanks" in user_input:
        response = "Aapka swagat hai. Aap aur kya jaanna chahenge?"
    else:
        response = f"Main aapka input '{data.input}' samajh nahi paaya, kripya kuch aur poochhiye."

    return {"output": response}
