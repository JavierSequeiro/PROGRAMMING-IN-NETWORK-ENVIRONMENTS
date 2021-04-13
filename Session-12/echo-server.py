import socket
import colorama
from colorama import Fore

IP = "127.0.0.1"
PORT = 8080

colorama.init(autoreset=True)
def process_client(s):
    req_raw = s.recv(2000)
    req = req_raw.decode()

    print("Message FROM CLIENT: ")
    print(Fore.GREEN + req)

#---- MAIN PROGRAM
#---- CONFIGURE SERVER

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ls.bind((IP, PORT))
ls.listen()

print("SEQ Server configured")

#---- LOOP
while True:
    print("Waiting for clients...")
    try:
        (client_socket, client_ip_port) = ls.accept()

    except KeyboardInterrupt:
        print("Server stopped")
        ls.close()
        exit()

    else:
        process_client(client_socket)

        client_socket.close()
