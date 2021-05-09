import http.client
import json
import http.server
import socketserver
import termcolor
from pathlib import Path
import jinja2
from urllib.parse import urlparse, parse_qs

SERVER = "rest.ensembl.org"
ENDPOINT = "/info/species"
PARAMETERS = "?content-type=application/json"

def read_html_file(filename):
    contents = Path(filename).read_text()
    return contents

def read_template_html_file(filename):
    contents = jinja2.Template(Path(filename).read_text())
    return contents
# Define the Server's port
PORT = 8080

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
        print(f"Keys: {arguments.keys()}")
        # Message to send back to the client
        SERVER = "rest.ensembl.org"
        PARAMETERS = "?content-type=application/json"
        context = {}
        if path_name == "/":
            contents = read_template_html_file("./HTML_FILES/index.html").render()
        # 1. GET N SPECIES OF VERTEBRATES
        elif path_name == "/listSpecies":
            endpoint = "/info/species"
            connection = http.client.HTTPConnection(SERVER)
            connection.request("GET", endpoint + PARAMETERS)
            response = connection.getresponse()
            vertebrates_list = []
            if response.status == 200:
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
                contents = read_template_html_file("./HTML_FILES/listSpecies.html").render(context=context)

        # 2. GET KARYOTYPE OF A SPECIE
        elif path_name == "/karyotype":
            endpoint = "/info/assembly/"
            specie = arguments["specie"][0]
            connection = http.client.HTTPConnection(SERVER)
            connection.request("GET", endpoint + specie + PARAMETERS)
            response = connection.getresponse()
            if response.status == 200:
                response = json.loads(response.read().decode())
                context["karyotype"] = response["karyotype"]
                contents = read_template_html_file("./HTML_FILES/karyotype.html").render(context=context)

        #3. GET CHROMOSOME LENGTH
        elif path_name == "/chromosomeLength":
            endpoint = "/info/assembly/"
            specie = arguments["specie"][0]
            connection = http.client.HTTPConnection(SERVER)
            connection.request("GET", endpoint + specie + PARAMETERS)
            response = connection.getresponse()
            if response.status == 200:
                response = json.loads(response.read().decode())
                for chromosome in response["top_level_region"]:
                    if chromosome["coord_system"] == "chromosome":
                        if chromosome["name"] == arguments["chromo"][0]:
                            context["chromosome_length"] = chromosome["length"]
                contents = read_template_html_file("./HTML_FILES/chromosome_length.html").render(context=context)




        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(contents.encode()))

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

