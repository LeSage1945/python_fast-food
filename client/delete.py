import requests

id = input("entrez l'ID de l'ement a supprimer : ")
endpoint = f"http://127.0.0.1:8000/produit/{id}/delete"
response = requests.delete(endpoint)
print(response.status_code, response.status_code == 204)