#Module for DNA projects
from pathlib import Path
def seq_ping():
    ok = "OK"
    return ok

def seq_read_fasta(filename):
    file_contents = Path(filename).read_text()
    useful_genome = file_contents[file_contents.find("\n"):].replace("\n", "")
    return useful_genome

def seq_len(filename):
    file_contents = Path(filename).read_text()
    useful_genome = file_contents[file_contents.find("\n"):].replace("\n","")
    return len(useful_genome)

def seq_len_sequence(sequence):
    return len(sequence)

def seq_count_bases(filename):
    file_contents = Path(filename).read_text()
    useful_genome = file_contents[file_contents.find("\n"):].replace("\n", "")
    return useful_genome.count("A"), useful_genome.count("C"), useful_genome.count("T"), useful_genome.count("G")

def seq_count_bases_sequence(dna):
    a = 0
    c = 0
    t = 0
    g = 0
    for i in dna:
        if i == "A":
            a +=1
        elif i == "C":
            c += 1
        elif i == "T":
            t += 1
        else:
            g += 1
    return a, c, t, g

def seq_reverse(sequence):
    return sequence[::-1]

def seq_complement(sequence):
    complement = ""
    for nucleotide in sequence:
        if nucleotide == "A":
            complement += "T"

        elif nucleotide == "T":
            complement += "A"

        elif nucleotide == "C":
            complement += "G"

        elif nucleotide == "G":
            complement += "C"
    return complement

def seq_check(sequence):
    for nucleotide in sequence:
        if nucleotide != "A" and nucleotide != "C" and nucleotide != "T" and nucleotide != "G":
            return False
    return True
