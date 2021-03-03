from Seq1 import Seq

print("-----| Practice 1, Exercise 5 |------")

seq1 = Seq()
seq2 = Seq("ACTGA")
seq3 = Seq("Invalid sequence")

print(f"Sequence 1: (Length: {Seq.len(seq1)}) {seq1}")
print(f" A: {Seq.count_base(seq1)[0]},  C: {Seq.count_base(seq1)[1]},  T: {Seq.count_base(seq1)[2]},  G: {Seq.count_base(seq1)[3]}")
print(f"Sequence 2: (Length: {Seq.len(seq2)}) {seq2}")
print(f" A: {Seq.count_base(seq2)[0]},  C: {Seq.count_base(seq2)[1]},  T: {Seq.count_base(seq2)[2]},  G: {Seq.count_base(seq2)[3]}")
print(f"Sequence 3: (Length: {Seq.len(seq3)}) {seq3}")
print(f" A: {Seq.count_base(seq3)[0]},  C: {Seq.count_base(seq3)[1]},  T: {Seq.count_base(seq3)[2]},  G: {Seq.count_base(seq3)[3]}")