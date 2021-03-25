from Client0 import Client
import colorama
from Seq1 import Seq

print("------| Practice 2, Exercise 5 |------")
s = Client("192.168.1.38", 8080)
gene_name = "U5"
gene_file = f"../Session-04/{gene_name}.txt"
useful_gene = Seq().read_fasta(gene_file)
colorama.init(autoreset=True)
client_info, server_info = s.debug_talk(f"Sending {gene_name} gene to the server...")
print(client_info)
print(server_info)
client, server = s.debug_talk(useful_gene)
print(client)
print(server)
