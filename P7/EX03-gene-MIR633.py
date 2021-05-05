import http.client
import json
gene_dict = {
    "FRAT1": "ENSG00000165879",
    "ADA": "ENSG00000196839",
    "FXN": "ENSG00000165060",
    "RNU6_269P": "ENSG00000212379",
    "MIR633": "ENSG00000207552",
    "TTTY4C": "ENSG00000228296",
    "RBMY2YP": "ENSG00000227633",
    "FGFR3": "ENSG00000068078",
    "KDR": "ENSG00000128052",
    "ANK2": "ENSG00000145362"
}
SERVER = "rest.ensembl.org"
ENDPOINT = "/sequence/id/"
ID = gene_dict["MIR633"]
PARAMETERS = "?content-type=application/json"
print(f"SERVER: {SERVER}")
print(f"URL {SERVER + ENDPOINT + PARAMETERS}")

connection = http.client.HTTPConnection(SERVER)
connection.request("GET", ENDPOINT + ID + PARAMETERS)
response = connection.getresponse()
print(f"Response received: {response.status} {response.reason}")
if response.status == 200:
    response = json.loads(response.read().decode())
    #dict_response = json.loads(response)
    #print(json.dumps(response, indent=4, sort_keys=True))
    print(f"Gene: {ID}")
    print("Description:", response["desc"])
    print("Bases: ", response["seq"])

elif response.status == 404:
    print("Check that the endpoint is correctly written")
