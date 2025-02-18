from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str

@app.post("/generate")
def generate_prompt(prompt_request: PromptRequest):
    payload = {
        "model": "llama3.2:latest",
        "prompt": prompt_request.prompt,
        "stream": False
    }
    try:
        response = requests.post("http://0.0.0.0:8080/api/generate", json=payload)
        response.raise_for_status()
        data = response.json()
        return {"response": data.get("response", "No response field found.")}
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))
