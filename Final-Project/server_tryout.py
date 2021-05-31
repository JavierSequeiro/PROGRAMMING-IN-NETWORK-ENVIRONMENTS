import http.client
import json
import http.server
import socketserver
import termcolor
from pathlib import Path
import jinja2
from urllib.parse import urlparse, parse_qs
from Seq1 import Seq

def read_html_file(filename):
    contents = Path(filename).read_text()
    return contents

def read_template_html_file(filename):
    contents = jinja2.Template(Path(filename).read_text())
    return contents
# Define the Server's port
PORT = 8080

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

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')
        termcolor.cprint(self.path, 'blue')

        # IN this simple server version:
        # We are NOT processing the client's request
        # It is a happy server: It always returns a message saying
        # that everything is ok
        o = urlparse(self.path)
        path_name = o.path
        arguments = parse_qs(o.query)
        print(f"Resources requested: {path_name}")
        print(f"Parameters: {arguments}")
        #print(f"Keys: {arguments.keys()}")
        # Message to send back to the client
        SERVER = "rest.ensembl.org"
        PARAMETERS = "?content-type=application/json"
        context = {}
        if path_name == "/":
            content_type = "text/html"
            contents = read_template_html_file("./HTML_FILES/index.html").render()

        # 1. GET N SPECIES OF VERTEBRATES
        elif path_name == "/listSpecies":
            endpoint = "/info/species"
            connection = http.client.HTTPConnection(SERVER)
            connection.request("GET", endpoint + PARAMETERS)
            response = connection.getresponse()
            vertebrates_list = []

            if response.status == 200:
                content_type = "text/html"
                response = json.loads(response.read().decode())
                context["number_species"] = len(response["species"])
                if "limit" in arguments.keys():
                    context["limit"] = int(arguments["limit"][0])
                    count = 0
                    for n in response["species"]:
                        if n["division"] == "EnsemblVertebrates":
                            vertebrates_list.append(n["common_name"])
                            count += 1
                        if count == context["limit"]:
                            break
                else:
                    context["limit"] = len(response["species"])
                    for i in response["species"]:
                        if i["division"] == "EnsemblVertebrates":
                            vertebrates_list.append(i["common_name"])
            context["species"] = vertebrates_list
            #JSON
            if "json" in arguments.keys():
                content_type = "application/json"
                contents = str(context)
            #HTML
            else:
                contents = read_template_html_file("./HTML_FILES/listSpecies.html").render(context=context)

        # 2. GET KARYOTYPE OF A SPECIE
        elif path_name == "/karyotype":
            endpoint = "/info/assembly/"
            specie = arguments["specie"][0]
            specie = specie.replace(" ", "_")
            connection = http.client.HTTPConnection(SERVER)
            connection.request("GET", endpoint + specie + PARAMETERS)
            response = connection.getresponse()
            try:
                if response.status == 200:
                    content_type = "text/html"
                    response = json.loads(response.read().decode())
                context["karyotype"] = response["karyotype"]
                #JSON
                if "json" in arguments.keys():
                    content_type = "application/json"
                    contents = str(context)
                #HTML
                else:
                    contents = read_template_html_file("./HTML_FILES/karyotype.html").render(context=context)
            except TypeError:
                if "json" in arguments.keys():
                    content_type = "application/json"
                    context["karyotype"] = "ERROR, MUST ENTER A VALID SPECIES"
                    contents = str(context)
                else:
                    content_type = "text/html"
                    contents = read_template_html_file("./HTML_FILES/Error.html").render()

        #3. GET CHROMOSOME LENGTH
        elif path_name == "/chromosomeLength":
            endpoint = "/info/assembly/"
            specie = arguments["specie"][0]
            connection = http.client.HTTPConnection(SERVER)
            connection.request("GET", endpoint + specie + PARAMETERS)
            response = connection.getresponse()
            count = 0
            if response.status == 200:
                response = json.loads(response.read().decode())
                #JSON APPLICATION
                if "json" in arguments.keys():
                    for chromosome in response["top_level_region"]:
                        if chromosome["coord_system"] == "chromosome" and chromosome["name"] == arguments["chromo"][0]:
                            json_chromosome = chromosome
                            count += 1
                    content_type = "application/json"
                    if count != 0:
                        contents = str(json_chromosome)
                    else:
                        context["chromosome"] = "ERROR, MUST CHECK THE NAME OF THE CHROMOSOME"
                        contents = str(context)

                #HTML APPLICATION
                else:
                    content_type = "text/html"
                    for chromosome in response["top_level_region"]:
                        if chromosome["coord_system"] == "chromosome" and chromosome["name"] == arguments["chromo"][0]:
                            context["chromosome_length"] = chromosome["length"]
                            count += 1
                    if count != 0:
                        contents = read_template_html_file("./HTML_FILES/chromosome_length.html").render(context=context)
                    else:
                        contents = read_template_html_file("./HTML_FILES/Error.html").render()
            else:
                if "json" in arguments.keys():
                    content_type = "application/json"
                    context["species"] = "ERROR, MUST CHECK THE NAME OF THE SPECIES"
                    contents = str(context)
                else:
                    content_type = "text/html"
                    contents = read_template_html_file("./HTML_FILES/Error.html").render()

        #4 GET HUMAN GENETIC SEQUENCE
        elif path_name == "/geneSeq":
            endpoint = "/sequence/id/"
            try:
                gene = arguments["gene"][0]
                id = gene_dict[gene]
                connection = http.client.HTTPConnection(SERVER)
                connection.request("GET", endpoint + id + PARAMETERS)
                response = connection.getresponse()
                if response.status == 200:
                    response = json.loads(response.read().decode())
                    context["gene_name"] = gene
                    context["sequence"] = response["seq"]
                    #JSON
                    if "json" in arguments.keys():
                        content_type = "application/json"
                        contents = str(context)
                    #HTML
                    else:
                        content_type = "text/html"
                        contents = read_template_html_file("./HTML_FILES/gene_sequence.html").render(context=context)
            except KeyError:
                #JSON
                if "json" in arguments.keys():
                    content_type = "application/json"
                    context["sequence"] = "ERROR, MUST ENTER A HUMAN GENE"
                    contents = str(context)
                #HTML
                else:
                    content_type = "text/html"
                    contents = read_template_html_file("./HTML_FILES/Error.html").render()

        #5 GET INFO ABOUT GENETIC SEQUENCE
        elif path_name == "/geneInfo":
            endpoint = "/sequence/id/"
            try:
                gene = arguments["gene"][0]
                id = gene_dict[gene]
                connection = http.client.HTTPConnection(SERVER)
                connection.request("GET", endpoint + id + PARAMETERS)
                response = connection.getresponse()
                if response.status == 200:
                    response = json.loads(response.read().decode())
                    gene_info = response["desc"]
                    gene_info_data = gene_info.split(":")
                    context["gene_name"] = gene
                    context["start"] = gene_info_data[3]
                    context["end"] = gene_info_data[4]
                    context["length"] = int(context["end"]) - int(context["start"])
                    context["id"] = id
                    context["chromosome_name"] = gene_info_data[2]
                    #JSON
                    if "json" in arguments.keys():
                        content_type = "application/json"
                        contents = str(context)
                    #HTML
                    else:
                        content_type = "text/html"
                        contents = read_template_html_file("./HTML_FILES/gene_info.html").render(context=context)
            except KeyError:
                if "json" in arguments.keys():
                    content_type = "application/json"
                    context["gene_name"] = "ERROR, INSERT THE NAME OF HUMAN GENE"
                    contents = str(context)
                else:
                    content_type = "text/html"
                    contents = read_template_html_file("./HTML_FILES/Error.html").render()

        # 6. CALCULATE GENE BASES PERCENTAGES
        elif path_name == "/geneCalc":
            endpoint = "/sequence/id/"
            try:
                gene = arguments["gene"][0]
                id = gene_dict[gene]
                connection = http.client.HTTPConnection(SERVER)
                connection.request("GET", endpoint + id + PARAMETERS)
                response = connection.getresponse()
                if response.status == 200:
                    response = json.loads(response.read().decode())
                    sequence = Seq(response["seq"])
                    context["gene_name"] = gene
                    context["length"] = sequence.len()
                    context["percentages"] = sequence.info()
                    if "json" in arguments.keys():
                        content_type = "application/json"
                        context["percentages"] = context["percentages"].strip("\n")
                        contents = str(context)
                    else:
                        content_type = "text/html"
                        contents = read_template_html_file("./HTML_FILES/gene_calc.html").render(context=context)
            except KeyError:
                if "json" in arguments.keys():
                    content_type = "application/json"
                    context["gene_name"] = "ERROR, YOU MUST ENTER A VALID NAME FOR THE GENE"
                    contents = str(context)
                else:
                    content_type = "text/html"
                    contents = read_template_html_file("./HTML_FILES/Error.html").render()

        else:
            content_type = "text/html"
            contents = read_template_html_file("./HTML_FILES/Error.html").render()

        #TO TEST EVERYTHING
        if not "json" in arguments.keys():
            #CHANGE MANUALLY THE FILE NAME TO TEST BASIC, MEDIUM
            file = Path("report-medium.txt").open("a")
            my_endpoint = path_name.strip("/")
            if path_name != "/favicon.ico" and path_name != "/":
                #my_endpoint = path_name.strip("/")
                file.write(f"----> {my_endpoint} endpoint \n")
                # CHANGE NUMBER OF TEST MANUALLY
                file.write(f"TEST \n\n")
                file.write(f"* Input: http://127.0.0.1:8080{self.path} \n"
                           f"\n"
                           f"* Output: \n\n")
                file.write(contents)
                file.write("\n\n"
                           "==================\n")
            else:
                pass
            file.close()

        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        self.send_header('Content-Type', content_type)
        if "json" in arguments.keys():
            #self.send_header('Content-Type', "application/json")
            self.send_header('Content-Length', len(str.encode(contents)))
        else:
            #self.send_header('Content-Type', "text/html")
            self.send_header('Content-Length', len(contents.encode()))
        # Define the content-type header:

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(contents.encode())

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()

