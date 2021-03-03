from Seq_Module import Seq

class Gene(Seq):
    """This class is derived from the Seq Class
       All the objects of class Gene will inherite
       the methods from the Seq class
    """
    def __init__(self, strbases, name=""):
        # -- Call first the Seq initilizer and then the
        # -- Gene init method
        super().__init__(strbases)
        self.name = name
        print("New gene created")

    def __str__(self):
        """Print the Gene name along with the sequence"""
        return self.name + "-" + self.strbases


# --- Main program
s1 = Seq("AGTACACTGGT")
g = Gene("CGTAAC", "FRAT1")

print(f"Sequence 1: {s1}")
#print(f"Length: {s1.len()}")
print(f"Gene: {g}")
#print(f"Length: {g.len()}")