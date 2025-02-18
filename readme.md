# Prompt Generation Microservice

This repository implements a prompt generation service using FastAPI. The project includes both synchronous and asynchronous endpoints to interface with external text generation services, along with a command-line interface for testing.

## Features

- **Synchronous Endpoint:**  
  Provides an API endpoint (`main.py`) that accepts user prompts, forwards them to an external service, and returns the generated response.
  
- **Asynchronous Endpoint:**  
  Implements an asynchronous endpoint (`server.py`) using the `httpx` library to forward prompts to an OLLAMA server.
  
- **Command-Line Client:**  
  A CLI tool (`main2.py`) that interacts with the synchronous API endpoint for local testing and debugging.

## Prerequisites

- Python 3.x
- FastAPI
- Uvicorn
- Requests
- HTTPx
- Pydantic

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. **Create and activate a virtual environment**
   - On Windows:
     ```bash
     python -m venv .venv
     .venv\Scripts\activate
     ```
   - On Unix or macOS:
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

3. **Install the dependencies**
   ```bash
   pip install fastapi uvicorn requests httpx pydantic
   ```

## Usage

### Running the Synchronous API (main.py)

Start the FastAPI server with Uvicorn:

bash
uvicorn main:app --reload


The synchronous endpoint will be available at:  
`http://0.0.0.0:8000/generate`

### Running the Asynchronous API (server.py)

Start the asynchronous server with Uvicorn:

bash
uvicorn server:app --reload


The asynchronous endpoint is available at:  
`http://localhost:8000/generate/`

### Using the Command-Line Client (main2.py)

Ensure that one of the APIs is running, then execute:

bash
python main2.py

The CLI will continuously prompt you to enter a text prompt. Type 'exit' to quit the client.

## File Structure

.
├── .gitignore # Ignores virtual environment and cache files.
├── main.py # Synchronous API endpoint implemented in FastAPI.
├── server.py # Asynchronous API endpoint using httpx.AsyncClient.
└── main2.py # Command-line client for local testing.


## License

[MIT License](LICENSE) *(or replace with your preferred license)*

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Open a pull request.

## Acknowledgements

- Built with [FastAPI](https://fastapi.tiangolo.com/).
- Thanks to all contributors and the open source community for their support.