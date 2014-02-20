#!/usr/bin/env python
import sys

# Declarations
n_feat = int(sys.argv[1])

# Initialize empty matrices to store r coefficients, number of rows, and a
# logical mask of the upper triangle of the matrix
means = [0.0 for i in range(n_feat)]
total_samples = [0 for i in range(n_feat)]

# Read a stream of records from standard input
for line in sys.stdin:
    
    # Extract key-value pair
    key_value = line.split('\t')
    key = key_value[0]
    value = key_value[1].split('_')
    
    # Extract feature number
    i = int(key[0])
    
    # Extract sum of values and number of rows
    i_sum = float(value[0])
    n_samples = int(value[1])
    
    # Fill matrices
    means[i] += i_sum
    total_samples[i] += n_samples

# For every feature with samples...
for i in range(0, n_feat):
    if total_samples[i] != 0:
        
        # ...compute the mean
        means[i] = means[i] / total_samples[i]
    
    # Define a new key
    new_key = str(i)
    
    # Print the result
    print'%s\t%f' % (new_key, means[i])