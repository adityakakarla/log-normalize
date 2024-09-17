#!/usr/bin/env python3

from LogNormalize_functions import *
import argparse
import humanfriendly
from timeit import default_timer as timer
import pandas as pd
import numpy as np

beginning_of_time = timer()

parser = argparse.ArgumentParser()
# ~~~~Module Required Arguments~~~~~ #
parser.add_argument("-F", "--filename",
                    type=str,
                    help="Name of the gct file to be processed")
parser.add_argument("-o", "--output_filename",
                    type=str,
                    help="The basename to use for output file",
                    default='result')
args = parser.parse_args()

print("~~~~~~~~~~~~~~~~~~~~~~")
print("Using arguments:")
print(args)
print("Now getting work done.")
print("~~~~~~~~~~~~~~~~~~~~~~")

try:
    df = pd.read_csv(args.filename, sep='\t', skiprows=2)

    log_transform = lambda n: np.log(n) if n > 0 else 0
    df.iloc[:, 2:] = df.iloc[:, 2:].applymap(log_transform)

    output_file = args.output_filename

    if not output_file.endswith('.gct'):
        output_file = output_file + '.gct'

    with open(output_file, 'w') as f:
        f.write("#1.2\n")
        f.write(f"{df.shape[0]}\t{df.shape[1] - 2}\n")
        df.to_csv(f, sep='\t', index=False)

    end_of_time = timer()
    print("We are done! Wall time elapsed:", humanfriendly.format_timespan(end_of_time - beginning_of_time))
except:
    print("Something went wrong. Exiting.")