import requests
import json
def send_message():
  url = "https://localhost:8080/process"
  message = {"message": "Hello MegaProgram!"}
  response = requests.post(url, json=message())
  print("Response from Go:", response.json())
if __name__ == "__main__":
  send_message
