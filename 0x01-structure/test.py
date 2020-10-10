#!env/bin/python3
import requests
# Url for get an user random
randomUserUrl = 'https://mxl96vlw4h.execute-api.us-east-1.amazonaws.com/Prod/user'
# Response a newUser random using the request.get and parsing to object with json() method
params = requests.get(randomUserUrl).json()
# Define the headers for sent an request to API clostering customer
headers = {'Content-Type': 'application/json'}
# Response a clostering user using the request.get and parsing to object with json() method
res = requests.post("https://mxl96vlw4h.execute-api.us-east-1.amazonaws.com/Prod/userpost", params=params, headers=headers).json()
# Print inf of user
print(f'user data sent: {params}')
# Print cluster user
print(f"clustering user: {res}")

