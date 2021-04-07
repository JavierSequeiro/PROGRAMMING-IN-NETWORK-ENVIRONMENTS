import socket
import colorama
from colorama import Fore
from Seq1 import Seq

PORT = 8080
IP = "127.0.0.1"
gene_list = ["U5.txt", "ADA.txt", "FRAT1.txt", "FXN.txt", "RNU6_269P.txt"]

colorama.init(autoreset=True)
sl = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sl.bind((IP, PORT))
sl.listen()
print("SEQ Server is configured!")
while True:
    print("Waiting for clients!")
    try:
        (client_socket, client_ip_port) = sl.accept()
    except KeyboardInterrupt:
        print("Server stopped by the user")
        sl.close()
        exit()

    else:
        msg_bytes = client_socket.recv(2048)
        print(msg_bytes)
        msg_string = msg_bytes.decode()
        useful_string = msg_string.replace("\n", "").replace("\r", "")
        print(useful_string == 'PING')
        if "PING" in msg_string:
            print(Fore.GREEN + "PING command")
            server_response = "OK!\n"
            print(server_response)
            client_socket.send(server_response.encode())

        elif "GET" in msg_string:
            for i in range(0, 4):
                if str(i) in msg_string:
                    seq_index = i
                    sequence = Seq.read_fasta(gene_list[seq_index])
                    print(Fore.GREEN + "GET")
                    print(sequence)
                    client_socket.send(sequence.encode())
        client_socket.close()
