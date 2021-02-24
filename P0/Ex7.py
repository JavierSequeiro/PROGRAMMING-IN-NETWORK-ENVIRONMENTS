import Seq0

folder = "../Session-04/"
gene  = "U5"

sequence = Seq0.seq_read_fasta(folder + gene + ".txt")[0:20]
print("-----| Exercise 5 |------ \n")
print(f"Gene {gene}")
print(f"Frag: {sequence}")
print(f"Comp: {Seq0.seq_complement(sequence)}")
