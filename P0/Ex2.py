import Seq0

filename = "../Session-04/U5.txt"
first_20_bases = Seq0.seq_read_fasta(filename)[0:20]
print(f"DNA file: {filename} \n"
      f"The first {len(first_20_bases)} bases are: \n"
      f"{first_20_bases}")
