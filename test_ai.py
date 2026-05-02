import requests
import json

url = "http://127.0.0.1:8000/chat"
payload = {"message": "Tell me a very short fun fact about space."}
headers = {"Content-Type": "application/json"}

try:
    print("Sending AI request...")
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f"Status Code: {response.status_code}")
    print(f"AI Reply: {response.json().get('bot_reply')}")
except Exception as e:
    print(f"Error: {e}")
