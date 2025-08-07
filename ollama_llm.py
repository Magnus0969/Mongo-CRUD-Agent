import requests
import json

OLLAMA_ENDPOINT = "http://127.0.0.1:11434"  # Replace with your endpoint if different
MODEL = "mongoai"

def query_ollama(prompt: str):
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(f"{OLLAMA_ENDPOINT}/api/generate", json=payload, stream = True)
    response.raise_for_status()
    return response.json()["response"]