from fastapi import FastAPI, Request
import httpx

app = FastAPI()
OLLAMA_SERVER_URL = "http://localhost:11434/api/generate"

@app.post("/generate/")
async def generate_text(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "")
    model = data.get("model", "llama3.2:latest")

    payload = {
        "model": model,
        "prompt": prompt
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(OLLAMA_SERVER_URL, json=payload)
        return response.json()
