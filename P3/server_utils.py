import colorama
from colorama import Fore
#from Seq1 import Seq

colorama.init(autoreset=True)
def modified_message(message):
    return message.replace("\n", "").replace("\r", "")

def ping(client_socket):
    print(Fore.GREEN + "PING command")
    server_response = "OK!\n"
    print(server_response)
    client_socket.send(server_response.encode())

def get_sequence(client_socket, index, gene_list):
    sequence = gene_list[index]
    print(Fore.GREEN + "GET")
    print(sequence)
    client_socket.send(sequence.encode())