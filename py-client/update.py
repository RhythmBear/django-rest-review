import requests

# Server Address
api_endpoint = "http://localhost:8000/api/products/4/update/"

data = {
    'title': "Product 105"
}

# Get UPdate Product Details
res = requests.put(api_endpoint, json=data
                        )
print(res.text)