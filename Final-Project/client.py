import http.client
import json
from pathlib import Path
PORT = 8080
SERVER = 'localhost'

print(f"\nConnecting to server: {SERVER}:{PORT}\n")

# Connect with the server
conn = http.client.HTTPConnection(SERVER, PORT)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
URL_TEST_LIST = ["/listSpecies?limit=&json=1", "/listSpecies?limit=10&json=1", "/karyotype?specie=human&json=1", "/karyotype?specie=FER&json=1",
                 "/chromosomeLength?specie=human&chromo=21&json=1", "/chromosomeLength?specie=human&chromo=34&json=1",
                 "/chromosomeLength?specie=whatever&chromo=34&json=1", "/geneSeq?gene=ADA&json=1", "/geneSeq?gene=WHATEVER&json=1",
                 "/geneInfo?gene=FRAT1&json=1", "/geneInfo?gene=WHATEVER&json=1", "/geneCalc?gene=FRAT1&json=1", "/geneCalc?gene=WHATEVER&json=1"]
for url in URL_TEST_LIST:
    try:
        conn.request("GET", url)
        #TESTS FOR 1
        #conn.request("GET", "/listSpecies?limit=&json=1")
        #conn.request("GET", "/listSpecies?limit=10&json=1")
        #TESTS FOR 2
        #conn.request("GET", "/karyotype?specie=human&json=1")
        #conn.request("GET", "/karyotype?specie=FER&json=1")
        #TESTS FOR 3
        #conn.request("GET", "/chromosomeLength?specie=human&chromo=21&json=1")
        #conn.request("GET", "/chromosomeLength?specie=human&chromo=34&json=1")
        #conn.request("GET", "/chromosomeLength?specie=whatever&chromo=34&json=1")
        #TESTS FOR 4
        #conn.request("GET", "/geneSeq?gene=ADA&json=1")
        #conn.request("GET", "/geneSeq?gene=WHATEVER&json=1")
        #TESTS FOR 5
        #conn.request("GET", "/geneInfo?gene=FRAT1&json=1")
        #conn.request("GET", "/geneInfo?gene=WHATEVER&json=1")
        #TESTS FOR 6
        #conn.request("GET", "/geneCalc?gene=FRAT1&json=1")
        #conn.request("GET", "/geneCalc?gene=WHATEVER&json=1")

    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()
    r1 = conn.getresponse()
    print(f"Response received!: {r1.status} {r1.reason}\n")

    # -- Read the response's body
    data1 = r1.read().decode("utf-8")
    json_data_string = json.dumps(data1)
    json_data_dict = json.loads(json_data_string)
    # -- Print the received data
    print(f"CONTENT: {json_data_dict}")



    file = Path("report-advanced.txt").open("a")
    my_endpoint = url.strip("/").split("?")[0]
    path_name = url.split("?")[0]
    if path_name != "/favicon.ico" and path_name != "/":
        # my_endpoint = path_name.strip("/")
        file.write(f"----> {my_endpoint} endpoint \n")
        # CHANGE NUMBER OF TEST MANUALLY
        file.write(f"TEST \n\n")
        file.write(f"* Input: http://127.0.0.1:8080{url} \n"
                   f"\n"
                   f"* Output: \n\n")
        file.write(json_data_dict)
        file.write("\n\n"
                   "==================\n")
    else:
        pass
    file.close()