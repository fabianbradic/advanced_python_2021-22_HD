import pandas as pd
from pathlib import Path
import plotly.graph_objects as go
from collections import deque
import numpy as np
from Bio import SeqIO
import re

def create_metrics(path_to_aa_file):
    amino_acids = pd.read_csv(Path(path_to_aa_file))
    amino_acids = amino_acids.rename(columns={"hydropathy index (Kyte-Doolittle method)": "hydropathy"})
    amino_acids = amino_acids.set_index("1-letter code")
    metrics = amino_acids.to_dict("dict")

    return metrics

def get_name(path_to_fasta_file):
    name = ""
    with open(Path(path_to_fasta_file)) as handle:
        for record in SeqIO.parse(handle,"fasta"):
            name = record.name
            return name


def get_sequence(path_to_fasta_file):
    sequence = ""
    with open(path_to_fasta_file,"r") as file:
        for line in file:
            if line[0] == ">":
                continue
            line = line.rstrip("\n")
            sequence += line

    bool_value = True
    if isinstance(sequence, str) == False: bool_value = False
    if any(i.isdigit() for i in sequence) == True: bool_value = False
    if "\n" in sequence == True: bool_value = False

    if bool_value == False: return bool_value
    return sequence
        


class Protein(object):
    def __init__(self, name, sequence, dictionary):
        self.name = name
        self.sequence = sequence
        self.dictionary = dictionary


    def plot(self, metric="hydropathy", window_size=10):

        y_data = []
        for aa in self.sequence:
            y_data.append(self.dictionary[metric][aa])

        sliding_window = deque([], maxlen = window_size)
        mean_list = []
        for y in y_data:
            sliding_window.append(y)
            mean = np.mean(list(sliding_window))
            mean_list.append(mean)

        data = [
            go.Bar(
                y = mean_list,
                x = [x for x in range(len(self.sequence))]
            )
        ]
        fig = go.Figure(data=data)
        fig.update_layout(template="plotly", title=self.name)
        return fig



if __name__ == '__main__':
    get_name("data/P32249.fasta")