# Array Transformations

# Generate an array with values from 1 to 50, reshape it into a 5x10 matrix.

# Flatten the above matrix into a 1D array.

# Sort an array in descending order.

import numpy as np

arr = np.arange(1, 51)  # Creates an array from 1 to 50

new_array = arr.reshape(5,10)

print('ARRAY after becoming matrix: ',new_array )

final_array = new_array.flatten()


print('Arrat after flattening: ',final_array)

final_final_array = np.sort(final_array)[::-1] # start , stop , step


print('sorted array: ', final_final_array)
