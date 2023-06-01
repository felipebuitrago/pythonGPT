import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("prompt", help="The prompt to send to chatGpt")
parser.add_argument("file_name", help="Name of the file to save .py")
args = parser.parse_args()

api_endpoint = "https://api.openai.com/v1/completions"
api_key = "your_api_key"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {str(api_key)}"
}

data = {
    "model": "text-davinci-003",
    "prompt": f"Write python script to {args.prompt}. Provide only code, no text",
    "max_tokens": 100,
    "temperature": 0
}

response = requests.post(api_endpoint, headers=headers, json=data)

if response.status_code == 200:
    
    response_text = response.json()["choices"][0]["text"]
    with open(args.file_name, "w") as file:
        file.write(response_text)
    print(response.json())

else:
    print(f"FAILED $$$ {str(response.status_code)}")