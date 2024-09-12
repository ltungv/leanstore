import argparse
import math
import os
import sys
from typing import List
import pandas as pd
import matplotlib.pyplot as plt

def parse_table(content:List[str]):


    table_content = [cnt.strip()[1:-1].replace(' ','').replace('-','').replace('\n', '').split('|') for cnt in content if cnt.strip().startswith('|') and cnt.strip().endswith('|')]


    formatted_header = ['t', 'OLTP TX', 'RF %', 'Abort%', 'OLAP TX', 'W_MiB', 'R_MiB', 'Instrs', 'Cycles', 'CPUs', 'L1_TX', 'LLC_TX', 'GHz', 'WAL_Gib/s', 'GCT_Gib/s', 'Space_G', 'GCT_Rounds']

    df = pd.DataFrame(columns=formatted_header,data=table_content[2:])
    return df


def plot_table(df: pd.DataFrame):
    add_plot_rows_on_top = 2

    d = int(math.ceil(len(df.columns) - 1) / 2) + add_plot_rows_on_top
    fig, axs = plt.subplots(d, 2, figsize=(3*d, 10*2))

    fig.suptitle('TPC-C plots')

    axs[0,0].plot(df['CPUs'], df["OLTP TX"]) 
    axs[0,0].set_xlabel('CPUs')
    axs[0,0].set_ylabel('OLTP TX')
    axs[0,0].grid(True)


    for i, col in enumerate(list(df.columns[1:]), start=add_plot_rows_on_top*2):
        # No need to print ax (it's an Axes object)
        row, col_idx = divmod(i, 2)
        ax = axs[row, col_idx]
        ax.plot(df['t'], df[col]) 
        ax.set_title(col)
        ax.set_xlabel('t')
        ax.set_ylabel(col)
        ax.grid(True)

    plt.tight_layout()
    plt.savefig("plt.png")
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parse TPC-C data from a text file.")
    parser.add_argument("file_path", type=str, nargs=1, help="Path to the TPC-C data file")
    args = parser.parse_args()

    file_path = str(args.file_path[0])


    try:
        with open(file_path, 'r') as f:
            file_lines = f.readlines()
            table = parse_table(content=file_lines)
            plot_table(df=table)
    except Exception as e:
        print(f"{e} dos not exist")
        sys.exit(1)

