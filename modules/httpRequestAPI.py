import requests
import json

r = requests.get("https://opentdb.com/api.php?amount=1&category=21&difficulty=easy&type=multiple")
print(r.status_code)
print(r.text)

question = json.loads(r.text)
print(question)
print((question['results'][0]['category']))