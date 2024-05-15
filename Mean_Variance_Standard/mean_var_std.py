import numpy as np

def calculate(numbers):
    """
    Calculate statistical measures across the axis and flattened state of a 3x3 matrix.

    Args:
    numbers (list): A list of 9 digits which will be converted to a 3x3 matrix.

    Returns:
    dict: Contains lists of mean, variance, standard deviation, max, min, and sum calculations.
    
    Raises:
    ValueError: If the input list does not contain exactly nine numbers.
    """
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers.")
    
    matrix = np.array(numbers).reshape((3, 3))

    calculations = {
        'mean': [list(np.mean(matrix, axis=0)), list(np.mean(matrix, axis=1)), np.mean(matrix)],
        'variance': [list(np.var(matrix, axis=0)), list(np.var(matrix, axis=1)), np.var(matrix)],
        'standard deviation': [list(np.std(matrix, axis=0)), list(np.std(matrix, axis=1)), np.std(matrix)],
        'max': [list(np.max(matrix, axis=0)), list(np.max(matrix, axis=1)), np.max(matrix)],
        'min': [list(np.min(matrix, axis=0)), list(np.min(matrix, axis=1)), np.min(matrix)],
        'sum': [list(np.sum(matrix, axis=0)), list(np.sum(matrix, axis=1)), np.sum(matrix)]
    }

    return calculations
