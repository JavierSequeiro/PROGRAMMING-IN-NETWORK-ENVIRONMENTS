class Seq:
    """A class for presenting sequences"""

    def __init__(self, strbases="NULL"):
        self.strbases = strbases
        if self.strbases == "NULL":
            print("NULL Seq created")

        elif Seq.is_valid_sequence(self):
            print("New sequence created!")
        else:
            self.strbases = "ERROR"
            print("ERROR")

    def is_valid_sequence(self):
        for nucleotide in self.strbases:
            if nucleotide != "A" and nucleotide != "C" and nucleotide != "T" and nucleotide != "G":
                return False
        return True

    @staticmethod
    def print_seqs(seq_list):
        data_list = []
        for sequence in seq_list:
            data = f"Sequence {seq_list.index(sequence)}: (Length: {Seq.len(sequence)}) {sequence}"
            data_list.append(data)
        return data_list

    def __str__(self):
        """Method called when the object is being printed"""

        # We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return 0
        else:
            return len(self.strbases)

    def count_base(self):
        #if self.strbases == "NULL" or self.strbases == "ERROR":
            #self.strbases = ""
        return self.strbases.count("A"), self.strbases.count("C"), self.strbases.count("T"), self.strbases.count("G")
