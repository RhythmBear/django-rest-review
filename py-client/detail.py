import requests

# Server Address
api_endpoint = "http://localhost:8000/api/"

# Get Request for product details
res = requests.get(api_endpoint + "products/2", 
                        )
print(res.text)