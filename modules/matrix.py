import numpy as np

def add_matrices(a, b):
    return np.add(a, b)

def subtract_matrices(a, b):
    return np.subtract(a, b)

def multiply_matrices(a, b):
    return np.dot(a, b)

def determinant(matrix):
    return np.linalg.det(matrix)

def inverse(matrix):
    return np.linalg.inv(matrix)
