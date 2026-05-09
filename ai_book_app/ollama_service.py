import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "qwen3:0.6b"

def ask_ollama(prompt: str):
    res = requests.post(OLLAMA_URL, json={
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    })
    return res.json()["response"]
