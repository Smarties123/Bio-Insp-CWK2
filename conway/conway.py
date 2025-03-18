"""
conway.py

Implements the Conway's Game of Life logic (no visuals).
"""

import numpy as np

class GameOfLife:
    def __init__(self, rows: int, cols: int, random_init: bool = False):
        self.rows = rows
        self.cols = cols
        if random_init:
            self.grid = np.random.randint(2, size=(rows, cols), dtype=np.int32)
        else:
            self.grid = np.zeros((rows, cols), dtype=np.int32)
    
    def count_neighbors(self, r, c):
        neighbors = 0
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                rr = r + dr
                cc = c + dc
                if 0 <= rr < self.rows and 0 <= cc < self.cols:
                    neighbors += self.grid[rr, cc]
        return neighbors

    def update(self):
        new_grid = np.zeros_like(self.grid)
        
        for r in range(self.rows):
            for c in range(self.cols):
                live_neighbors = self.count_neighbors(r, c)
                if self.grid[r, c] == 1:
                    # Survive if 2 or 3 neighbors
                    if live_neighbors in [2, 3]:
                        new_grid[r, c] = 1
                else:
                    # Birth if exactly 3 neighbors
                    if live_neighbors == 3:
                        new_grid[r, c] = 1
        
        self.grid = new_grid
