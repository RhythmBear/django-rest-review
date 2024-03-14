import requests

# Server Address
api_endpoint = "http://localhost:8000/api/products/5/delete/"


data = {
    "title": "Product 105"
}

# Get UPdate Product Details
res = requests.delete(api_endpoint, json=data
                        )
print(res.text)