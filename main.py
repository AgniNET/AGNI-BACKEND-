from fastapi import FastAPI, Request
import requests

app = FastAPI()

# 🔐 AGNI Telegram Configuration
BOT_TOKEN = "7065457101:AAFyMtSLy7ArYIq25ajiVX2U9UZy3QxREo"
CHAT_ID = "7665788919"

# 🔁 Send text to Telegram channel
def send_to_telegram(text: str):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text
    }
    requests.post(url, data=payload)

# 🎯 AGNI input handler
@app.post("/process")
async def process_input(req: Request):
    data = await req.json()
    user_input = data.get("input", "")

    # 🤖 AGNI Intelligence Layer
    if "video" in user_input.lower():
        reply = "🎥 Video generation pipeline activated based on your input."
    elif "image" in user_input.lower():
        reply = "🖼️ Image rendering module initiated."
    elif "audio" in user_input.lower() or "music" in user_input.lower():
        reply = "🎵 Audio generation/selection module is working."
    elif "link" in user_input.lower():
        reply = "🔗 I'm preparing downloadable content links."
    elif "delete" in user_input.lower():
        reply = "🗑️ Deletion command received. Confirming with admin..."
    else:
        reply = "✅ AGNI has received your message and is processing it intelligently."

    # 📤 Telegram Logging
    send_to_telegram(f"📩 User Input:\n{user_input}\n\n🧠 AGNI Reply:\n{reply}")

    return {"output": reply}

