# Ollama FastAPI Integration

This project provides a simple FastAPI application that acts as an intermediary between your local Ollama instance and clients (e.g., Postman or custom applications). It allows you to:

- **Set a System Prompt:** Configure a system prompt for your model to guide its responses.
- **Generate Text:** Send prompts to your Ollama model and receive generated responses.

The app is designed to support a longer context window and a generous HTTP timeout to accommodate the demands of larger prompts and more complex responses.

## Why This Project?

- **Local Model Integration:** Easily integrate and experiment with locally hosted language models powered by Ollama.
- **Flexible Configuration:** Dynamically set system prompts to adjust the model's behavior for specific tasks (e.g., answering in one word, following instructions, etc.).
- **Enhanced Usability:** Use tools like Postman or curl to interact with your model via a straightforward API.
- **Robust and Extendable:** With built-in logging and configurable parameters (like context window size and timeout), the project is ready for further development and debugging.

## Example Usage

### 1. Start Your Ollama Server

Ensure that Ollama is installed and running on your machine. By default, it listens on `http://localhost:11434`.

```bash
ollama serve
```

### 2. Run the FastAPI App
Start the FastAPI application with Uvicorn:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### 3. Set a System Prompt
Use Postman or curl to set a system prompt for your model. For example, to instruct the model to answer questions in one word:

- Endpoint: POST http://localhost:8000/set_system_prompt

- Headers: Content-Type: application/json
- Body:
```bash
{
  "system_prompt": "Only answer questions in one word: True or False."
}
```

### 4. Generate Text
Now, generate a response from your model by sending a prompt:

- Endpoint: POST http://localhost:8000/generate
- Headers: Content-Type: application/json
- Body:

```bash
{
  "prompt": "Does the Earth rotate?"
}
```

The response will include the generated answer, formatted according to the system prompt you set.

## Customization
- Model Selection: The model used for requests is defined in the MODEL_NAME variable in main.py. Change it as needed.
- Context Window: The ctx_size parameter is set to 8192 to allow longer inputs. Adjust this value based on your model’s capabilities.
- Timeouts: The HTTP client timeout is set to 120 seconds. This can be increased or decreased as required.