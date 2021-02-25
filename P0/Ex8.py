import Seq0

folder = "../Session-04/"
genes_list = ["RNU6_269P", "U5", "ADA", "FRAT1", "FXN"]
print("-----| Exercise 8 |------ \n")
for gene in genes_list:
    A, C, T, G = Seq0.seq_count_bases(folder + gene + ".txt")
    bases_dict = {"A": A, "C": C, "T": T, "G": G}
    max_base = max([A, C, G, T])
    for k, v in bases_dict.items():
        if v == max_base:
            print(f"Gene {gene}: Most frequent Base: {k}")
