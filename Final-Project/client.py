import http.client
import json

PORT = 8080
SERVER = 'localhost'

print(f"\nConnecting to server: {SERVER}:{PORT}\n")

# Connect with the server
conn = http.client.HTTPConnection(SERVER, PORT)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
try:
    #TEST FOR 1
    #conn.request("GET", "/listSpecies?limit=&json=1")
    #conn.request("GET", "/listSpecies?limit=10&json=1")
    #TEST FOR 2
    #conn.request("GET", "/karyotype?specie=human&json=1")
    #conn.request("GET", "/karyotype?specie=FER&json=1")
    #TEST FOR 3
    #conn.request("GET", "/chromosomeLength?specie=human&chromo=21&json=1")
    #conn.request("GET", "/chromosomeLength?specie=human&chromo=34&json=1")
    #
    #TEST FOR 4
    #conn.request("GET", "/geneSeq?gene=ADA&json=1")
    #conn.request("GET", "/geneSeq?gene=WHATEVER&json=1")
    #TEST FOR 5
    #conn.request("GET", "/geneInfo?gene=FRAT1&json=1")
    #conn.request("GET", "/geneInfo?gene=WHATEVER&json=1")
    #TEST FOR 6
    conn.request("GET", "/geneCalc?gene=FRAT1&json=1")
    #conn.request("GET", "/geneCalc?gene=WHATEVER&json=1")

except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()
r1 = conn.getresponse()
print(f"Response received!: {r1.status} {r1.reason}\n")

# -- Read the response's body
data1 = r1.read().decode("utf-8")
json_data = json.dumps(data1)

# -- Print the received data
print(f"CONTENT: {json_data}")