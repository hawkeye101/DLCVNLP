# Numpy Assignment

# Problem 1
import numpy as np
def vander_matrix(A):
    dimension = np.size(A)
    # Use below if input is not 1d array
    # A = np.reshape(A,[1,dimension])
    output = np.empty([dimension,dimension])
    for i in range(dimension):
        for j in range(dimension):
            output[i,j] = A[i]**(dimension-j-1)
    return output

A = [1,2,3,4]
print(vander_matrix(A))

# Problem 2
def moving_average(A,k): # k is size of window
    n = np.size(A)
    values = np.empty(n-k+1)
    for i in range(n-k+1):
        values[i] = np.average(A[i:i+k])
    return values

A = [1,2,3,4,5,6,7,8]
print(moving_average(A,3))