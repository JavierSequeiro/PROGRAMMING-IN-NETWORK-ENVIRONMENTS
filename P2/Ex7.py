from Client0 import Client
from Seq1 import Seq
import colorama
from colorama import Fore

print("------| Practice 2, Exercise 7 |------")
s = Client("192.168.1.38", 8080)
m = Client("192.168.1.38", 8081)
gene_name = "FRAT1"
gene_file = f"../Session-04/{gene_name}.txt"
colorama.init(autoreset=True)
useful_gene = Seq().read_fasta(gene_file)
sending_message, server_info = s.debug_talk(f"Sending {gene_name} gene to the server...")
sending_message2, server_info2 = m.debug_talk(f"Sending {gene_name} gene to the server...")
print(f"Gene {gene_name}: {Fore.BLUE + useful_gene}")

for i in range(0, 10):
    if i % 2 != 0:
        odd_gene, response = s.debug_talk(f"Fragment {i+1}: {useful_gene[10*i:10 + 10*i]}")
        print(odd_gene)
    else:
        even_gene, response = m.debug_talk(f"Fragment {i + 1}: {useful_gene[10 * i:10 + 10 * i]}")
        print(even_gene)


