class Seq:
    """A class for presenting sequences"""
    def __init__(self, strbases):
        self.strbases = strbases
        if Seq.is_valid_sequence(self):
            print("New sequence created!")
        else:
            self.strbases = "ERROR"
            print("ERROR")

    def is_valid_sequence(self):
        for nucleotide in self.strbases:
            if nucleotide != "A" and nucleotide != "C" and nucleotide != "T" and nucleotide != "G":
                return False
        return True

    def __str__(self):
        """Method called when the object is being printed"""

        # We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        return len(self.strbases)

s1 = Seq("AGTACACTGGT")
s2 = Seq("CGTDAAC")

print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")