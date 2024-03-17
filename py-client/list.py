import requests

# Server Address
api_endpoint = "http://localhost:8000/api/products/"

# Get Request for product details
res = requests.get(api_endpoint)
print(res.json())