from Seq1 import Seq

print("-----| Practice 1, Exercise 5 |------")

seq1 = Seq()
seq2 = Seq("ACTGA")
seq3 = Seq("Invalid sequence")
sequence_list = [seq1, seq2, seq3]

for sequence in sequence_list:
    a, c, t, g = Seq.count_base(sequence)
    bases_dict = {"A": a, "C": c, "T": t, "G": g, }
    print(f"Sequence {sequence_list.index(sequence)}: (Length: {Seq.len(sequence)}) {sequence}")
    print(bases_dict)
