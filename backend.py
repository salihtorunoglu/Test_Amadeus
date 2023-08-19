import requests
import json

# This code sends a GET request to https://flights-api.buraky.workers.dev/ and checks the HTTP status code of the response. If the HTTP status code is 200, the request is successful. If the HTTP status code is not 200, the request is unsuccessful.
response = requests.get("https://flights-api.buraky.workers.dev/")

if response.status_code == 200:
    print("Request is successful")
else:
    print("Request is not successful")
    exit()

# I've used the json.loads() function to convert the JSON response into a Python dictionary

data = json.loads(response.content)

print("Response:",str(type(data)))
print(data)
for flight in data["data"]:
    print("Flight:")
    print("     Id:", flight["id"])
    print("     From:", flight["from"])
    print("     To:", flight["to"])
    print("     Date:", flight["date"])

# This code checks if there is a Content-Type header in the response, then it checks if the value of the Content-Type is application/json

if "Content-Type" in response.headers:
    print("'Content-Type' header does exist in the Response")
else:
    print("Content-Type' header does not exist in the Response")
    exit()

if response.headers.get("Content-Type") == "application/json":
    print("The value of the Content-Type is application/json.")
else:
    print("The value of the Content-Type is not application/json .")