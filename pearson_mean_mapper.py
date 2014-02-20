#!/usr/bin/env python
import sys

# Declarations
n_feat = int(sys.argv[1])

# Initialize an empty vector to store feature sums
sums = [0.0 for i in range(n_feat)]

# Initialize variable for number of samples
n_samples = 0

# Read a stream of records from standard input
for line in sys.stdin:
    
    # Count number of rows
    n_samples += 1    
    
    # Split data into features
    feat = line.split('\t')
    
    # For every feature...
    for i in range(0, n_feat):
        
        # ...if it has a value...
        if feat[i] != 'NULL':

            # ...sum it to previous values
            sums[i] += float(feat[i])

# For evey feature...
for i in range(0, n_feat):
        
    # ...define a key-value pair
    key = str(i)
    value = str(sums[i]) + '_' + str(n_samples)
    
    # Print the result
    print '%s\t%s' % (key, value)