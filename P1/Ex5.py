from Seq1 import Seq

def print_counts(i, sequence):
    print(f"Sequence {i}: (Length: {Seq.len(sequence)}) {sequence}")
    print( f" A: {Seq.count_base(sequence)[0]},  C: {Seq.count_base(sequence)[1]},  T: {Seq.count_base(sequence)[2]},  G: {Seq.count_base(sequence)[3]}")


print("-----| Practice 1, Exercise 5 |------")

seq1 = Seq()
seq2 = Seq("ACTGA")
seq3 = Seq("Invalid sequence")
sequence_list = [seq1, seq2, seq3]
print_counts(1, seq1)
print_counts(2, seq2)
print_counts(3, seq3)

# WITH A FOR LOOP
for i in range(1, len(sequence_list) + 1):
    print_counts(i, sequence_list[i - 1])

