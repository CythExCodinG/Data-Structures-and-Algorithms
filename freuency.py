import numpy as np
import pandas as pd

# Original frequencies
frequencies = [5, 9, 13, 21, 20, 15, 8, 3]

# Constructing the Grouping Table with equal lengths
grouping_table = {
    "f": frequencies,
    "Pairs from 1st": [sum(frequencies[i:i+2]) for i in range(0, len(frequencies) - 1)] + [None],
    "Pairs from 2nd": [sum(frequencies[i:i+2]) for i in range(1, len(frequencies) - 1)] + [None],
    "Triples from 1st": [sum(frequencies[i:i+3]) for i in range(0, len(frequencies) - 2)] + [None, None],
    "Triples from 2nd": [sum(frequencies[i:i+3]) for i in range(1, len(frequencies) - 2)] + [None, None],
    "Triples from 3rd": [sum(frequencies[i:i+3]) for i in range(2, len(frequencies) - 2)] + [None, None]
}

# Creating DataFrame for the Grouping Table
grouping_df = pd.DataFrame(grouping_table)

# Find the maximum values in each column to identify modal class candidates
max_values = grouping_df.max()

grouping_df, max_values
