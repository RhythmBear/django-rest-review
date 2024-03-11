import requests

# Server Address
api_endpoint = "http://localhost:8000/api/"

data = {
    "title": "Product 105"
}

# Get Request for product details
res = requests.post(api_endpoint, json=data 
                        )
print(res.text)