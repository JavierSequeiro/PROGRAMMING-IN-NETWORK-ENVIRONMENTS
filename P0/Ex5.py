import Seq0

folder = "../Session-04/"
gene_list = ["RNU6_269P", "U5", "ADA", "FRAT1", "FXN"]
print("-----| Exercise 5 |------ \n")
for gene in gene_list:
    bases_dict = {}
    filename = folder + gene + ".txt"
    A, C, T, G = Seq0.seq_count_bases(filename)
    bases_dict["A"] = A
    bases_dict["T"] = T
    bases_dict["C"] = C
    bases_dict["G"] = G
    print(f"Gene {gene}: {bases_dict}")
