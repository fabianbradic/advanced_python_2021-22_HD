from collections import Counter
import csv
import matplotlib.pyplot as plt
import pandas as pd
import sys



def aa_count(input_file,output_file_name="aa_count.csv"):
    
    counter = Counter()
    with open(input_file,"r") as file:
        for line in file:
            if line[0] == ">":
                continue
            line = line.rstrip("\n") # removes linebreak character
            counter = counter + Counter(line)
    with open(output_file_name,"w") as output:
        aa_writer = csv.DictWriter(output, fieldnames=["aa","count"], extrasaction="ignore")
        aa_writer.writeheader()
        for key,item in counter.items():
            aa_writer.writerow({"aa":key, "count":item})
    print(f"Saved data as {output_file_name}")


def create_bar_plot(input_file):
    df = pd.read_csv(input_file)
    plt.bar(df["aa"], df["count"])
    plt.ylabel("Counts")
    plt.xlabel("Amino Acids")
    plt.savefig("aa_counts_bar_plot.png")
    print("Saved plot as aa_counts_bar_plot.png")


if __name__ == '__main__':
    input_file_path = sys.argv[1]
    aa_count(input_file_path)
    create_bar_plot("aa_count.csv")
