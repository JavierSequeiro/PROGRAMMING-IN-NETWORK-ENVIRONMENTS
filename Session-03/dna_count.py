def count_nucleotides(dna):
    a = 0
    c = 0
    t = 0
    g = 0
    for i in dna:
        if i == "A":
            a +=1
        elif i == "C":
            c += 1
        elif i == "T":
            t += 1
        else:
            g += 1
    return a, c, t, g

dna = "CATGTAGACTAG"
a, c, t, g = count_nucleotides(dna)
# helps us to not run the loops so many times
print(f"A: {a} \n"
      f"C: {c} \n"
      f"T: {t} \n"
      f"G: {g} \n")

print(f"Total length: {len(dna)}")
