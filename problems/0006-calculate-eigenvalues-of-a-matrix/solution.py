import numpy as np

def calculate_eigenvalues(matrix):
    eigenvalues = np.linalg.eigvals(matrix)
    eigenvalues = sorted(eigenvalues, reverse=True)
    return [float(x) for x in eigenvalues]