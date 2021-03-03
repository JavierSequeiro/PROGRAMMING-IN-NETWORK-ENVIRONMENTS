from Seq_Module import Seq


def print_seqs(seq_list):
    data_list = []
    for sequence in seq_list:
        data = f"Sequence {seq_list.index(sequence)}: (Length: {Seq.len(sequence)}) {sequence}"
        data_list.append(data)
    return data_list

seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
for gene in print_seqs(seq_list):
    print(gene)