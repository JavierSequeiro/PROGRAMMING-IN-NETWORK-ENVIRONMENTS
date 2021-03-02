class Seq:
    """A class for presenting sequences"""
    def __init__(self, strbases):
        self.strbases = strbases
        count = 0
        for nucleotide in strbases:
            if nucleotide != "A" and nucleotide != "C" and nucleotide != "T" and nucleotide != "G":
                count += 1
        if count != 0:
            self.strbases = "ERROR"
            print("ERROR")
        #else:
            #print("New sequence created!")

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

seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
for gene in print_seqs(seq_list):
    print(gene)