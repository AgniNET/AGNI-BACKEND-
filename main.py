from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to AGNI backend"}

@app.post("/process/")
async def process_input(
    text: str = Form(None),
    file: UploadFile = File(None)
):
    # Placeholder logic – बाद में AGNI modules से बदलेंगे
    result = {}
    if text:
        result["text_response"] = f"Received text: {text}"
    if file:
        content = await file.read()
        result["file_name"] = file.filename
        result["file_size"] = len(content)

    return JSONResponse(content=result)

# अगर लोकली चलाना हो:
# if __name__ == "__main__":
#     uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
