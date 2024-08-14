import requests

endpoint = "http://127.0.0.1:8000/produit/5/update"
response = requests.put(endpoint, json={'nom':'pop smok', 'content':'rap', 'prix':'12345'})
print(response.json())
print(response.status_code)