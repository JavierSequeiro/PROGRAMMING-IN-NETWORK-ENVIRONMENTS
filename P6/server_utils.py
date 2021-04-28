import colorama
from colorama import Fore
from Seq1 import Seq

colorama.init(autoreset=True)
def modified_message(message):
    return message.replace("\n", "").replace("\r", "")

def ping(client_socket):
    print(Fore.GREEN + "PING command")
    server_response = "OK!\n"
    print(server_response)
    client_socket.send(server_response.encode())

def get_sequence(client_socket, index, gene_list):
    sequence = gene_list[index]
    print(Fore.GREEN + "GET")
    print(sequence)
    client_socket.send(sequence.encode())

def info(client_socket, sequence):
    print(Fore.GREEN + "INFO")
    complete_nuc_info = ""
    useful_seq = Seq(sequence)
    A, C, T, G = useful_seq.count_base()

    seq_info = f"Sequence: {sequence}\n"
    complete_nuc_info += seq_info

    seq_len = f"Total length: {len(sequence)}\n"
    complete_nuc_info += seq_len

    nucleotides_list = [A, C, T, G]
    nucleotides_names = ["A", "C", "T", "G"]
    for i in range(0, 4):
        nuc_info = f"{nucleotides_names[i]}: {nucleotides_list[i]} ({(nucleotides_list[i] * 100) / len(sequence)}%)\n"
        complete_nuc_info += nuc_info
    print(complete_nuc_info)
    client_socket.send(complete_nuc_info.encode())

def complementary(client_socket, sequence):
    print(Fore.GREEN + "COMP")

    useful_seq = Seq(sequence)
    complementary_seq = useful_seq.complement()
    print(complementary_seq)
    client_socket.send(complementary_seq.encode())

def reverse(client_socket, sequence):
    print(Fore.GREEN + "REV")

    useful_seq = Seq(sequence)
    reverse_seq = useful_seq.reverse()
    print(reverse_seq)
    client_socket.send(reverse_seq.encode())

def gene(client_socket, gene):
    print(Fore.GREEN + "GENE")
    sequence = Seq()
    try:
        complete_seq = sequence.read_fasta(f"{gene}.txt")
        print(complete_seq)
        client_socket.send(complete_seq.encode())
    except FileNotFoundError:
        print("THE CLIENT MUST ENTER AN AVAILABLE GENE")
        not_available_message = "YOU MUST ENTER AN AVAILABLE GENE\n [U5, FRAT1, FXN, RNU6_269P]"
        client_socket.send(not_available_message.encode())
