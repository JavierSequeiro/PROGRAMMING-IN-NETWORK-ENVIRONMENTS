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
        else:
            print("New sequence created!")

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