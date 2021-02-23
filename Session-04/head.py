from pathlib import Path

FILENAME = input("Enter the name of the file containing the gene info: ")

genome = Path(FILENAME).read_text()
gene_info = ""
for c in genome:
    if c == "\n":
        print(gene_info)
        break
    else:
        gene_info = gene_info + c
