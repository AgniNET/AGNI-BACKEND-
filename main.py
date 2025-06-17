from fastapi import FastAPI, Request
from telegram_utils import send_to_telegram_bot

app = FastAPI()

@app.post("/relay/")
async def relay(request: Request):
    data = await request.json()
    option = data.get("option")
    user_input = data.get("input")

    result = send_to_telegram_bot(option, user_input)
    return {"result": result}
