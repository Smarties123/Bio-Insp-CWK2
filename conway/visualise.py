"""
visualise.py

Simple text or matplotlib-based visualisation for GOL.
"""

import numpy as np
import matplotlib.pyplot as plt

def print_grid(grid: np.ndarray):
    rows, cols = grid.shape
    for r in range(rows):
        row_str = "".join("#" if grid[r,c] else "." for c in range(cols))
        print(row_str)

def plot_grid(grid: np.ndarray, title="Game of Life"):
    plt.imshow(grid, cmap='binary')
    plt.title(title)
    plt.axis('off')
    plt.show()
