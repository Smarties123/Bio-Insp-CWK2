"""
experiment.py

A single function that runs our DEAP GA to evolve a PyTorch neural network.
"""

from .deap_ga import run_deap_ga

def run_experiment(population_size=20, generations=10):
    """
    Runs a demonstration experiment with DEAP-based GA 
    on a small PyTorch net (5->3->2).
    """
    best_indiv, best_fitness = run_deap_ga(
        input_size=5,
        hidden_size=3,
        output_size=2,
        pop_size=population_size,
        generations=generations,
        cx_prob=0.5,
        mut_prob=0.2
    )
    return best_indiv, best_fitness
