import sys
from pathlib import Path
# -------- START of inconvenient addon block --------
# This block is not necessary if you have installed your package
# using e.g. pip install -e (requires setup.py)
# or have a symbolic link in your sitepackages (my preferend way)
sys.path.append(
    str(Path(__file__).parent.parent.resolve())
)
# It make import peak_finder possible
# This is a demo hack for the course :)
# --------  END of inconvenient addon block  --------

import peak_finder

def test_find_peaks():
    peaks = peak_finder.basic.find_peaks([0, 2, 1])
    assert peaks == [2] 

def test_cointains_None():
    peaks = peak_finder.basic.find_peaks([0,1,3,None,0])
    assert peaks == False

def test_contains_touple():
    peaks = peak_finder.basic.find_peaks([0,2,4,(1,2,3),5])
    assert peaks == "touple"



from exercises.day4.protein import create_metrics, get_sequence, Protein
import plotly

def test_create_metrics():
    metrics = create_metrics(Path("data/amino_acid_properties.csv"))
    assert isinstance(metrics, dict) == True

def test_get_sequence():
    sequence = get_sequence(Path("data/P32249.fasta"))
    assert isinstance(sequence, str)

def test_plotting():
    name = "GP183_HUMAN G-protein coupled receptor 183"
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