def read_file(file):
    nucleotides_list = []
    with open(file, "r") as f:
        for line in f:
            #sline = line.rstrip("\n")
            line = line.replace("\n", "")
            for c in line:
                nucleotides_list.append(c)
    return nucleotides_list

def count_nucletides(nuc_list):
    a = 0
    c = 0
    t = 0
    g = 0
    for i in nuc_list:
        if i == "A":
            a += 1
        elif i == "C":
            c += 1
        elif i == "T":
            t += 1
        else:
            g += 1
    return a, c, t, g

file = "dna.txt"
a, c, t, g = count_nucletides(read_file(file))

print(f"A: {a} \n"
      f"C: {c} \n"
      f"T: {t} \n"
      f"G: {g} \n")

print(f"Number of bases: {len(set(read_file(file)))}")
