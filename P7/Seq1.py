class Seq:
    """A class for presenting sequences"""
    NULL_SEQUENCE = "NULL"
    INVALID_SEQUENCE = "ERROR"
    def __init__(self, strbases=NULL_SEQUENCE):
        self.strbases = strbases
        if self.strbases == Seq.NULL_SEQUENCE:
            print("NULL Seq created")

        elif Seq.is_valid_sequence(self):
            print("New sequence created!")
        else:
            self.strbases = Seq.INVALID_SEQUENCE
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
        if self.strbases == Seq.NULL_SEQUENCE or self.strbases == Seq.INVALID_SEQUENCE:
            return 0
        else:
            return len(self.strbases)

    def count_base(self):
        a, c, t, g = 0, 0, 0, 0
        if self.strbases == Seq.NULL_SEQUENCE or self.strbases == Seq.INVALID_SEQUENCE:
            return a, c, t, g
        else:
            return self.strbases.count("A"), self.strbases.count("C"), self.strbases.count("T"), self.strbases.count("G")

    def count_bases_no_count(self):
        a, c, g, t = 0, 0, 0, 0
        if (not self.strbases == Seq.NULL_SEQUENCE) and (not self.strbases == Seq.INVALID_SEQUENCE):
            for ch in self.strbases:
                if ch == "A":
                    a += 1
                elif ch == "C":
                    c += 1
                elif ch == "G":
                    g += 1
                else:
                    t += 1
        return a, c, g, t
    def reverse(self):
        if self.strbases == Seq.NULL_SEQUENCE or self.strbases == Seq.INVALID_SEQUENCE:
            return self.strbases
        else:
            return self.strbases[::-1]

    def complement(self):
        if self.strbases == Seq.NULL_SEQUENCE or self.strbases == Seq.INVALID_SEQUENCE:
            return self.strbases
        else:
            complement_gene = ""
            for nucleotide in self.strbases:
                if nucleotide == "A":
                    complement_gene += "T"
                elif nucleotide == "T":
                    complement_gene += "A"
                elif nucleotide == "C":
                    complement_gene += "G"
                else:
                    complement_gene += "C"
            return complement_gene

    def read_fasta(self, file):
        from pathlib import Path
        file_contents = Path(file).read_text()
        self.strbases = file_contents[file_contents.find("\n"):].replace("\n", "")
        return self.strbases

    def info(self):
        complete_nuc_info = ""
        #useful_seq = Seq(sequence)
        A, C, T, G = self.strbases.count_base()

        seq_info = f"Sequence: {self.strbases}\n"
        complete_nuc_info += seq_info

        seq_len = f"Total length: {len(self.strbases)}\n"
        complete_nuc_info += seq_len

        nucleotides_list = [A, C, T, G]
        nucleotides_names = ["A", "C", "T", "G"]
        for i in range(0, 4):
            nuc_info = f"{nucleotides_names[i]}: {nucleotides_list[i]} ({(nucleotides_list[i] * 100) / len(self.strbases)}%)\n"
            complete_nuc_info += nuc_info
        return complete_nuc_info
