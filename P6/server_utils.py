import colorama
from colorama import Fore
from Seq1 import Seq
from pathlib import Path
import jinja2

colorama.init(autoreset=True)
def modified_message(message):
    return message.replace("\n", "").replace("\r", "")

def ping(client_socket):
    print(Fore.GREEN + "PING command")
    server_response = "OK!\n"
    print(server_response)
    client_socket.send(server_response.encode())

def get_sequence(seq_number, gene_list):
    sequence = gene_list[int(seq_number)]
    context = {"number": seq_number,
               "sequence": sequence}
    contents = read_template_html_file("./HTML_FILES/get.html").render(context=context)
    return contents

def read_template_html_file(filename):
    contents = jinja2.Template(Path(filename).read_text())
    return contents


def info(sequence):
    useful_seq = Seq(sequence)
    complete_nuc_info = ""
    seq_len = f"Total length: {len(sequence)}\n"
    complete_nuc_info += seq_len

    A, C, T, G = useful_seq.count_base()
    context = {
        "operation": "INFO"
    }

    nucleotides_list = [A, C, T, G]
    nucleotides_names = ["A", "C", "T", "G"]
    for i in range(0, 4):
        nuc_info = f"{nucleotides_names[i]}: {nucleotides_list[i]} ({(nucleotides_list[i] * 100) / len(sequence)}%)\n"
        complete_nuc_info += nuc_info
    context["sequence"] = complete_nuc_info
    contents = read_template_html_file("./HTML_FILES/operation.html").render(context=context)
    return contents

def complementary(client_socket, sequence):
    print(Fore.GREEN + "COMP")

    useful_seq = Seq(sequence)
    complementary_seq = useful_seq.complement()
    print(complementary_seq)
    client_socket.send(complementary_seq.encode())

def reverse(sequence):
    print(Fore.GREEN + "REV")

    useful_seq = Seq(sequence)
    reverse_seq = useful_seq.reverse()
    print(reverse_seq)
    client_socket.send(reverse_seq.encode())

def gene(gene):
    sequence = Seq()
    complete_seq = sequence.read_fasta(f"./Sequences/{gene}.txt")
    context = {
        "gene_name": gene,
        "gene_contents": sequence.strbases
    }
    contents = read_template_html_file("./HTML_FILES/gene.html").render(context=context)
    return contents