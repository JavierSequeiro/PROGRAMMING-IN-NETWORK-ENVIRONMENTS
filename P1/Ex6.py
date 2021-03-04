from Seq1 import Seq

print("-----| Practice 1, Exercise 5 |------")

seq1 = Seq()
seq2 = Seq("ACTGA")
seq3 = Seq("Invalid sequence")
sequence_list = [seq1, seq2, seq3]

for sequence in sequence_list:
    bases_dict = {"A": Seq.count_base(sequence)[0], "C": Seq.count_base(sequence)[1], "T": Seq.count_base(sequence)[2], "G": Seq.count_base(sequence)[3], }
    print(f"Sequence {sequence_list.index(sequence)}: (Length: {Seq.len(sequence)}) {sequence}")
    print(bases_dict)
