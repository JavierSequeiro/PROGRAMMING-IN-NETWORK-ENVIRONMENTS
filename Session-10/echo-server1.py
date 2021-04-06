import socket
import colorama
from colorama import Fore

PORT = 8080
IP = "192.168.1.39"

colorama.init(autoreset=True)
sl = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sl.bind((IP, PORT))
sl.listen()
print("The server is configured!")
while True:
    print("Waiting for connections...")
    try:
        (client_socket, client_ip_port) = sl.accept()
    except KeyboardInterrupt:
        print("Server stopped by the user.")
        sl.close()
        exit()

    else:
        print("A client has connected to the server! ")
        msg_bytes = client_socket.recv(2048)
        msg_string = msg_bytes.decode()
        print(f"Message received: {Fore.GREEN + msg_string}")

        server_response = f"ECHO: {msg_string}"
        client_socket.send(server_response.encode())
        client_socket.close()