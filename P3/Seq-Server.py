import socket
import colorama
#from colorama import Fore
#from Seq1 import Seq
import server_utils

PORT = 8080
IP = "127.0.0.1"
#seq_list = ["ACTTTGGATGATCAT", "CGAAATTGCTAGCA", "TAAAACGCCTGATGC", "GGTACGGAATCGAT", "ATCCCCCCGAAT"]
seq_list = ["ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA", "AAAAACATTAATCTGTGGCCTTTCTTTGCCATTTCCAACTCTGCCACCTCCATCGAACGA", "CAAGGTCCCCTTCTTCCTTTCCATTCCCGTCAGCTTCATTTCCCTAATCTCCGTACAAAT", "CCCTAGCCTGACTCCCTTTCCTTTCCATCCTCACCAGACGCCCGCATGCCGGACCTCAAA", "AGCGCAAACGCTAAAAACCGGTTGAGTTGACGCACGGAGAGAAGGGGTGTGTGGGTGGGT"]

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
        msg_string = msg_bytes.decode()
        useful_string = server_utils.modified_message(msg_string)
        separate_strings = useful_string.split(" ")
        #print(separate_strings[0] == 'INFO')
        #print(separate_strings[1])

        if "PING" == server_utils.modified_message(msg_string):
            server_utils.ping(client_socket)

        elif separate_strings[0] == "GET":
            server_utils.get_sequence(client_socket, int(separate_strings[1]), seq_list)

        elif separate_strings[0] == "INFO":
            server_utils.info(client_socket, separate_strings[1])

        elif separate_strings[0] == "COMP":
            server_utils.complementary(client_socket, separate_strings[1])

        elif separate_strings[0] == "REV":
            server_utils.reverse(client_socket, separate_strings[1])

        elif separate_strings[0] == "GENE":
            server_utils.gene(client_socket, separate_strings[1])
        client_socket.close()

