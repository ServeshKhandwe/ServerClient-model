import requests

while True:
    prompt = input("Enter your prompt (or type 'exit' to quit): ")
    if prompt.lower() == 'exit':
        break
    payload = {
        "prompt": prompt
    }
    response = requests.post("http://0.0.0.0:8000/generate", json=payload)
    if response.status_code == 200:
        data = response.json()
        print("Response:", data.get("response", "No response field found."))
    else:
        print("Error:", response.status_code, response.text)