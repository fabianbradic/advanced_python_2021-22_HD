from exercises.day4.protein import create_metrics, get_name, get_sequence, Protein
import plotly
from pathlib import Path

def test_get_name():
    name = get_name("data/P32249.fasta")
    assert isinstance(name, str) == True

def test_create_metrics():
    metrics = create_metrics(Path("data/amino_acid_properties.csv"))
    assert isinstance(metrics, dict) == True

def test_get_sequence():
    sequence = get_sequence(Path("data/P32249.fasta"))
    assert isinstance(sequence, str)

def test_plotting():
    name = get_name("data/P32249.fasta")
    sequence= get_sequence("data/P32249.fasta")
    metrics = create_metrics(Path("data/amino_acid_properties.csv"))
    testobj = Protein(name, sequence, metrics)
    fig = testobj.plot()
    assert isinstance(fig, plotly.graph_objs._figure.Figure)


if __name__ == '__main__':
    print("test")
    seq = get_sequence(Path("data/P32249.fasta"))
    print(seq)
    test_create_metrics()