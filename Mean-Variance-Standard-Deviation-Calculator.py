import numpy as np

def calculate(list_input):
    # Ensure list has exactly 9 numbers
    if len(list_input) != 9:
        raise ValueError("List must contain nine numbers.")

    # Convert list into 3x3 numpy array
    matrix = np.array(list_input).reshape(3, 3)

    # Build the dictionary of results
    calculations = {
        'mean': [
            matrix.mean(axis=0).tolist(),   # column-wise
            matrix.mean(axis=1).tolist(),   # row-wise
            matrix.mean().item()            # flattened
        ],
        'variance': [
            matrix.var(axis=0).tolist(),
            matrix.var(axis=1).tolist(),
            matrix.var().item()
        ],
        'standard deviation': [
            matrix.std(axis=0).tolist(),
            matrix.std(axis=1).tolist(),
            matrix.std().item()
        ],
        'max': [
            matrix.max(axis=0).tolist(),
            matrix.max(axis=1).tolist(),
            matrix.max().item()
        ],
        'min': [
            matrix.min(axis=0).tolist(),
            matrix.min(axis=1).tolist(),
            matrix.min().item()
        ],
        'sum': [
            matrix.sum(axis=0).tolist(),
            matrix.sum(axis=1).tolist(),
            matrix.sum().item()
        ]
    }

    return calculations
