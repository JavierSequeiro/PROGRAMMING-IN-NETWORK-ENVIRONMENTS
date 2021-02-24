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
