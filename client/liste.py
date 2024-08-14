import requests

endpoint = "http://127.0.0.1:8000/produit/liste"
response = requests.get(endpoint)
print(response.json())
print(response.status_code)