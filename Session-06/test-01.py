from Seq0 import *

seq1 = "ATTCCCGGGG"
A, C, T, G = seq_count_bases_sequence(seq1)
if seq_check(seq1):
    print(f"Seq:    {seq1}")
    print(f"  Rev : {seq_reverse(seq1)}")
    print(f"  Comp: {seq_complement(seq1)}")
    print(f"  Length: {seq_len_sequence(seq1)}")
    print(f"    A: {A}")
    print(f"    T: {T}")
    print(f"    C: {C}")
    print(f"    G: {G}")
else:
    print("NOT A CORRECT GENETIC SEQUENCE")