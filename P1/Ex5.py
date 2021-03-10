from Seq1 import Seq

def print_counts(i, sequence):
    print(f"Sequence {i}: (Length: {Seq.len(sequence)}) {sequence}")
    a, c, t, g = Seq.count_bases_no_count(sequence)
    print( f" A: {a},  C: {c},  T: {t},  G: {g}")


print("-----| Practice 1, Exercise 5 |------")

seq1 = Seq()
seq2 = Seq("ACTGA")
seq3 = Seq("Invalid sequence")

# NO LOOP
#print_counts(1, seq1)EXERCISE
#print_counts(2, seq2)
#print_counts(3, seq3)

# WITH A FOR LOOP
sequence_list = [seq1, seq2, seq3]
for i in range(1, len(sequence_list) + 1):
    print_counts(i, sequence_list[i - 1])

