#import socket
#import server_utils
from Client0 import Client
print("-----| Practice 3, Exercise 7 |------")
PORT = 8080
IP = "127.0.0.1"

module_seq_list = ["PING", "GET", "INFO", "COMP", "REV", "GENE"]
seq_list = ["ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA", "AAAAACATTAATCTGTGGCCTTTCTTTGCCATTTCCAACTCTGCCACCTCCATCGAACGA", "CAAGGTCCCCTTCTTCCTTTCCATTCCCGTCAGCTTCATTTCCCTAATCTCCGTACAAAT", "CCCTAGCCTGACTCCCTTTCCTTTCCATCCTCACCAGACGCCCGCATGCCGGACCTCAAA", "AGCGCAAACGCTAAAAACCGGTTGAGTTGACGCACGGAGAGAAGGGGTGTGTGGGTGGGT"]

client = Client(IP, PORT)
print(client)

#PING TESTING
print("* Testing PING...")
print(client.talk("PING"))

#GET TESTING
print("* Testing GET...")
for i in range(0, 5):
    sequence = client.talk(f"GET {i}")
    print(f"GET {i}: {sequence}")

#INFO TESTING
print("* Testing INFO...")
print(client.talk(f"INFO {seq_list[0]}"))

#COMP TESTING
print("* Testing COMP...")
print(f"COMP {seq_list[0]}")
print(client.talk(f"COMP {seq_list[0]}\n"))

#REV TESTING
print("Testing REV...")
print(f"REV {seq_list[0]}")
print(client.talk(f"REV {seq_list[0]}\n"))

#GENE TESTING
gene_list = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
print("* Testing GENE...")
for gene in gene_list:
    print(f"GENE {gene}")
    print(client.talk(f"GENE {gene}\n"))





