# Statistical Operations

# Create an array of 100 random numbers.

# Find the mean, median, variance, and standard deviation.


import numpy as np

arr = np.random.rand(100)

summation = arr.sum()

mean = arr.mean()

std = arr.std()

variance = arr.var()

median = np.median(arr)

print('sum: ',summation)
print('mean: ',mean)
print('std: ',std)
print('variance: ',variance)
print('median: ',median)