import logging
import httpx
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# -----------------------------------------------------------------------------
# Logging Setup
# -----------------------------------------------------------------------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ollama-fastapi")

# -----------------------------------------------------------------------------
# Global Variables
# -----------------------------------------------------------------------------
# Set the Ollama model to be used for all requests.
MODEL_NAME = "deepseek-r1:7b"

# -----------------------------------------------------------------------------
# Data Models
# -----------------------------------------------------------------------------
class PromptRequest(BaseModel):
    prompt: str

class SystemPromptRequest(BaseModel):
    system_prompt: str

# -----------------------------------------------------------------------------
# FastAPI Application
# -----------------------------------------------------------------------------
app = FastAPI()

# A simple in-memory store for system prompts per model.
system_prompts = {}

@app.post("/set_system_prompt")
async def set_system_prompt(request: SystemPromptRequest):
    """
    Sets a system prompt for the current model that will be used in subsequent requests.
    """
    system_prompts[MODEL_NAME] = request.system_prompt
    logger.info(f"System prompt set for {MODEL_NAME}: {request.system_prompt}")
    return {"message": "System prompt set successfully."}

@app.post("/generate")
async def generate_text(request: PromptRequest):
    """
    Generates text using the defined Ollama model, taking into account any system prompt
    previously set. Increases the context window and sets a longer HTTP timeout.
    """
    # The URL where Ollama is listening.
    ollama_url = "http://localhost:11434/api/generate"

    # Retrieve the stored system prompt for the current model (if any).
    system_prompt = system_prompts.get(MODEL_NAME, "")

    # Define the payload with an increased context window.
    payload = {
        "model": MODEL_NAME,
        "system": system_prompt,
        "prompt": request.prompt,
        "stream": False,
        "ctx_size": 8192  # Increased context window.
    }

    # Set a longer timeout (e.g., 120 seconds).
    timeout = httpx.Timeout(120.0)
    headers = {"Content-Type": "application/json"}

    logger.info(f"Sending request to Ollama: {payload}")

    try:
        async with httpx.AsyncClient(timeout=timeout) as client:
            response = await client.post(ollama_url, json=payload, headers=headers)
            logger.info(f"Received status code {response.status_code} from Ollama")

            response.raise_for_status()

            result = response.json()
            logger.info(f"Ollama response: {result}")

        return {"response": result.get("response", "")}

    except httpx.HTTPStatusError as e:
        error_msg = f"Error from Ollama: {e.response.text}"
        logger.error(error_msg)
        raise HTTPException(status_code=e.response.status_code, detail=error_msg)
    except Exception as e:
        error_msg = f"Internal Server Error: {str(e)}"
        logger.error(error_msg)
        raise HTTPException(status_code=500, detail=error_msg)
