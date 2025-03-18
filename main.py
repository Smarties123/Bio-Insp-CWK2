"""
main.py

Entry point that orchestrates:
1) A brief run of Conway’s Game of Life.
2) A Genetic Algorithm test run to evolve a small neural net population.
3) (Optional) Integration demonstration: using the neural net to interpret GoL states.
"""

import numpy as np
import argparse

from conway.conway import GameOfLife
from conway.visualise import print_grid
from conway.pygame_visual import GOLPyGame
from neural_evolution.experiment import run_experiment


def demo_conway_text():
    # Quick text-based GOL demonstration
    rows, cols = 10, 10
    gol = GameOfLife(rows, cols, random_init=True)
    print("Initial Game of Life State:")
    print_grid(gol.grid)
    
    for step in range(3):
        gol.update()
        print(f"\nState after step {step+1}:")
        print_grid(gol.grid)

def demo_conway_pygame():
    # Optional real-time PyGame GOL
    gol_pygame = GOLPyGame(rows=30, cols=30, cell_size=20, random_init=True)
    gol_pygame.run()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pygame", action="store_true", help="Use PyGame real-time GOL demo")
    args = parser.parse_args()

    # 1) Demonstrate GOL
    if args.pygame:
        print("Running PyGame-based GOL. Close the window to continue.")
        demo_conway_pygame()
    else:
        demo_conway_text()

    # 2) Run a GA experiment with DEAP + PyTorch
    print("\n--- Starting DEAP-based GA experiment ---")
    best_indiv, best_fitness = run_experiment(
        population_size=10,
        generations=5
    )
    print("GA experiment completed.")
    print("Best fitness achieved:", best_fitness)
    print("Best individual's param vector (first few values):", best_indiv[:10]) # Show partial


if __name__ == "__main__":
    main()
