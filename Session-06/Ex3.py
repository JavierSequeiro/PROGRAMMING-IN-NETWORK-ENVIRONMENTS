class Seq:
    """A class for presenting sequences"""
    def __init__(self, strbases):
        self.strbases = strbases
        print("New sequence created!")

    def __str__(self):
        """Method called when the object is being printed"""

        # We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        return len(self.strbases)

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

print("List 1:")
print_seqs(seq_list1)
for gene in print_seqs(seq_list1):
    print(gene)

print()
print("List 2:")
print_seqs(seq_list2)
for gene in print_seqs(seq_list2):
    print(gene)