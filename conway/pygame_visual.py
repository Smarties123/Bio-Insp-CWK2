"""
pygame_visual.py

Real-time PyGame animation for Conway's Game of Life.
Close the window to stop.
"""

import pygame
import numpy as np
from .conway import GameOfLife

class GOLPyGame:
    def __init__(self, rows=50, cols=50, cell_size=10, random_init=True):
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        self.gol = GameOfLife(rows, cols, random_init=random_init)

        pygame.init()
        self.screen = pygame.display.set_mode((cols * cell_size, rows * cell_size))
        pygame.display.set_caption("Conway's Game of Life (PyGame)")

        self.clock = pygame.time.Clock()
        self.running = True

    def draw_grid(self):
        for r in range(self.rows):
            for c in range(self.cols):
                cell_val = self.gol.grid[r, c]
                color = (0, 255, 0) if cell_val == 1 else (0, 0, 0)
                rect = pygame.Rect(c*self.cell_size, r*self.cell_size, self.cell_size, self.cell_size)
                pygame.draw.rect(self.screen, color, rect)

    def run(self):
        while self.running:
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            # Update GOL
            self.gol.update()

            # Draw
            self.screen.fill((0,0,0))
            self.draw_grid()
            pygame.display.flip()

            # Limit FPS, e.g. 10 updates/sec
            self.clock.tick(10)
        
        pygame.quit()
