import requests
from getpass import getpass

# Create a call to get the Authentication Token
auth_url = "http://localhost:8000/api/auth/"

auth_data = {
    'username': 'admin',
    'password': getpass()
}


auth_response = requests.post(auth_url, json=auth_data)
print(auth_response.json())

if auth_response.status_code == 200:
    # Server Address
    token = auth_response.json()['token']
    headers = {
        'Authorization': f"Bearer {token}"
    }

    api_endpoint = "http://localhost:8000/api/products/"

    # Get Request for product details
    res = requests.get(api_endpoint, headers=headers)
    print(res.json())

else:
    print("Failed to Login")