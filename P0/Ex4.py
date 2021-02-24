import Seq0

folder = "../Session-04/"
genes_list = ["RNU6_269P", "U5", "ADA", "FRAT1", "FXN"]
print("-----| Exercise 4 |------ \n")
for gene in genes_list:
    filename = folder + gene + ".txt"
    A, C, T, G = Seq0.seq_count_bases(filename)
    print(f"Gene {gene}: \n"
          f"A: {A} \n"
          f"C: {C} \n"
          f"T: {T} \n"
          f"G: {G} \n")