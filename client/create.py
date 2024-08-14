import requests

endpoint = "http://127.0.0.1:8000/produit/create/"
response = requests.post(endpoint, json={'nom':'pop', 'content':'rap', 'prix':'0000'})
print(response.json())
print(response.status_code)