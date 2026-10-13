import numpy as np

def reshape_matrix(a: list[list[int | float]], new_shape: tuple[int, int]) -> list[list[int | float]]:
    try:
        reshaped_matrix = np.reshape(a, new_shape)
        return reshaped_matrix.tolist()
    except ValueError:
        return []