from Seq1 import Seq
from pathlib import Path

print("-----| Practice 1, Exercise 9 |------")

file = "../Session-04/U5.txt"
sequence = Seq()
sequence.read_fasta(file)

bases_dict = {"A": Seq.count_base(sequence)[0], "C": Seq.count_base(sequence)[1], "T": Seq.count_base(sequence)[2], "G": Seq.count_base(sequence)[3], }
print(f"Sequence: (Length: {Seq.len(sequence)}) {sequence}")
print(bases_dict)
print(f"Rev: {Seq.reverse(sequence)}")
print(f"Comp: {Seq.complement(sequence)}")