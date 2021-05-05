import http.client
import json

SERVER = "rest.ensembl.org"
ENDPOINT = "/info/ping"
PARAMETERS = "?content-type=application/json"
print(f"SERVER: {SERVER}")
print(f"URL {SERVER + ENDPOINT + PARAMETERS}")

connection = http.client.HTTPConnection(SERVER)
connection.request("GET", ENDPOINT + PARAMETERS)
response = connection.getresponse()
print(f"Response received: {response.status} {response.reason}")
answer_decoded = response.read().decode()
dict_response = json.loads(answer_decoded)
if dict_response["ping"] == 1:
    print("PING OK! THE DATA BASE IS RUNNING!! ")
else:
    print("DATA BASE IS DOWN...")