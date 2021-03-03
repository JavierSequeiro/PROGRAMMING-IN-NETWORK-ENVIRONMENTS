import termcolor
from Seq_Module import Seq
def print_seqs(seq_list):
    data_list = []
    for sequence in seq_list:
         data = f"Sequence {seq_list.index(sequence)}: (Length: {Seq.len(sequence)}) {sequence}"
         data_list.append(data)
    return data_list

def generate_seqs(pattern, number):
    pattern_list = []
    gene = ""
    for c in range(0, number):
        gene += pattern
        pattern_list.append(Seq(gene))
    return pattern_list

seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

termcolor.cprint("List 1:", "blue")
print_seqs(seq_list1)
for gene in print_seqs(seq_list1):
    termcolor.cprint(gene, "blue")


termcolor.cprint("List 2:", "green")
print_seqs(seq_list2)
for gene in print_seqs(seq_list2):
    termcolor.cprint(gene, "green")