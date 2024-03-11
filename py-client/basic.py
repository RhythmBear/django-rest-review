import requests

# Server Address
api_endpoint = "http://localhost:8000/api/"

# Get Request 
# # Calling the Server
# response = requests.get(api_endpoint, 
#                         params={'abc': 123}, 
#                         json={"query": "Hello World"}
#                         )

# # print(response.text)
# print(response.status_code)
# print(response.text)

# POst Request 
res = requests.post(api_endpoint, 
                    json={
                        'id': 12, 
                        'title': "Product 12",
                        "content": "Owner of id 12", 
                        'price': 12
                        }
                        )
print(res.text)