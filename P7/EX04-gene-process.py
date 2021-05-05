import http.client
import json
from Seq1 import Seq

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
PARAMETERS = "?content-type=application/json"

connection = http.client.HTTPConnection(SERVER)

try:
    user_gene = input("Enter the gene that you want to analyze: ")
    id = gene_dict[user_gene]
    connection.request("GET", ENDPOINT + id + PARAMETERS)
    response = connection.getresponse()
    print(f"SERVER: {SERVER}")
    print(f"URL: {SERVER + ENDPOINT + PARAMETERS}")
    print(f"Response received!: {response.status} {response.reason} \n")
    if response.status == 200:
        response = json.loads(response.read().decode())
        print(f"Gene: {user_gene}")
        print("Description:", response["desc"])
        sequence = Seq(response["seq"])
        print(sequence.info())
        print(f"Most frequent base: {sequence.most_frequent_base()}")

except KeyError:
    print("The gene is not inside the data base. Choose between the following:", list(gene_dict.keys()))

