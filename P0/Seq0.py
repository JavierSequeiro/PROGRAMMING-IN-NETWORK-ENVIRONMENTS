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

def seq_count_bases(filename):
    file_contents = Path(filename).read_text()
    useful_genome = file_contents[file_contents.find("\n"):].replace("\n", "")
    return useful_genome.count("A"), useful_genome.count("C"), useful_genome.count("T"), useful_genome.count("G")

def seq_reverse(sequence):
    return sequence[::-1]
