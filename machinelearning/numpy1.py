# Matrix Operations

# Create a 5x5 matrix filled with random numbers. done

# Compute the sum, mean, and standard deviation of the matrix. done

# Extract the third row and second column from the matrix.

# Multiply two random 3x3 matrices together.



import numpy as np
arr = np.array([[1,2,3,4,5],[3,4,7,9,3],[1,3,4,5,7],[1,2,8,6,4],[9,8,7,1,7]])

print('array: ',arr)

sum = arr.sum()
mean = arr.mean()
deviation = arr.std()

element = arr[2:,1]


print('sum: ', sum)
print('mean: ', mean)
print('deviation: ', deviation)
print('element: ', element)


