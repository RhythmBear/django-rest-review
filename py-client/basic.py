import requests

api_endpoint = "http://localhost:8000/api/"


response = requests.get(api_endpoint, 
                        params={'abc': 123}, 
                        json={"query": "Hello World"}
                        )

# print(response.text)
print(response.status_code)
print(response.text)