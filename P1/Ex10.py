from Seq1 import Seq

print("-----| Practice 1, Exercise 10 |------")

gene_list =["U5", "ADA", "FRAT1", "FXN", "RNU6_269P" ]
folder = "../Session-04/"

for gene in gene_list:
    file = folder + gene + ".txt"
    sequence = Seq()
    sequence.read_fasta(file)
    A, C, T, G = Seq.count_base(sequence)
    max_base = max([A, C, T, G])
    nucleotides_dict = {"A": A, "C": C, "T": T, "G": G}
    for k, v in nucleotides_dict.items():
        if v == max_base:
            print(f"Gene {gene}: Most frequent base: {k}")
