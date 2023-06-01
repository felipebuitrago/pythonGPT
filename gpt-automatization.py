import requests

api_endpoint = "https://api.openai.com/v1/completions"
api_key = ""

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {str(api_key)}"
}

data = {
    "model": "text-davinci-003",
    "prompt": "Write python script for hello fucking world",
    "max_tokens": 100,
    "temperature": 0
}

response = requests.post(api_endpoint, headers=headers, json=data)

if response.status_code == 200:
    print(response.json())
else:
    print(f"FAILED $$$ {str(response.status_code)}")