from Client0 import Client
from Seq1 import Seq
import colorama

print("------| Practice 2, Exercise 5 |------")
s = Client("192.168.1.38", 8080)
gene_name = "FRAT1"
gene_file = f"../Session-04/{gene_name}.txt"
colorama.init(autoreset=True)
useful_gene = Seq().read_fasta(gene_file)
client, server = s.debug_talk(useful_gene)
print(f"Gene {gene_name}: {client}")

for i in range (0, 5):
    fragment = f"Fragment {i+1}: {useful_gene[10*i:10 + 10*i]}"
    gene, response = s.debug_talk(fragment)
    print(gene)