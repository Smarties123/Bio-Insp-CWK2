"""
deap_ga.py

Implements a Genetic Algorithm with DEAP. We'll treat the PyTorch net's parameters
as our genotype.
"""

import random
import numpy as np
import torch
from deap import base, creator, tools

from .neural_net_torch import NeuralNetTorch

# 1) Define a Fitness class and Individual class
creator.create("FitnessMax", base.Fitness, weights=(1.0,))  # single objective, maximize
creator.create("Individual", np.ndarray, fitness=creator.FitnessMax)

def init_individual(input_size, hidden_size, output_size):
    """
    Creates a new random individual's param vector
    by building a NeuralNetTorch, then returning a flattened param vector.
    """
    net = NeuralNetTorch(input_size, hidden_size, output_size)
    # param vector shape depends on # of weights/bias in net
    param_vec = net.get_param_vector()
    return creator.Individual(param_vec)

def evaluate_individual(indiv, input_size=5, hidden_size=3, output_size=2):
    """
    Convert param vector -> PyTorch net -> compute a fitness.
    Here, we do something trivial: feed random inputs & measure closeness to a target.
    """
    net = NeuralNetTorch(input_size, hidden_size, output_size)
    net.set_param_vector(indiv)

    # Example fitness: negative MSE to a random target
    # The GA will maximize, so we do negative MSE
    # let's do 3 random inputs
    fitness_score = 0.0
    target = torch.tensor([[1.0, -1.0]])
    for _ in range(3):
        x = torch.randn(1, input_size)
        out = net(x)
        mse = torch.mean((out - target)**2)
        fitness_score += -mse.item()
    # Return a tuple
    return (fitness_score,)

def mutate_individual(indiv, indpb=0.1, sigma=0.1):
    """
    Gaussian mutation for each param with probability indpb.
    sigma is the std dev for the normal distribution.
    """
    size = len(indiv)
    for i in range(size):
        if random.random() < indpb:
            indiv[i] += random.gauss(0, sigma)
    return (indiv,)

def crossover_individual(ind1, ind2):
    """
    One-point crossover on the param array. 
    """
    size = len(ind1)
    cxpoint = random.randint(1, size-1)
    ind1[cxpoint:], ind2[cxpoint:] = ind2[cxpoint:].copy(), ind1[cxpoint:].copy()
    return ind1, ind2

def setup_deap(input_size, hidden_size, output_size, pop_size=20, cx_prob=0.5, mut_prob=0.2):
    toolbox = base.Toolbox()

    # Register: individual init, population init
    toolbox.register("individual", init_individual, input_size, hidden_size, output_size)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    # Register the evaluation, crossover, mutation, selection
    toolbox.register("evaluate", evaluate_individual, input_size=input_size, hidden_size=hidden_size, output_size=output_size)
    toolbox.register("mate", crossover_individual)
    toolbox.register("mutate", mutate_individual, indpb=0.1, sigma=0.1)
    toolbox.register("select", tools.selTournament, tournsize=3)

    return toolbox

def run_deap_ga(input_size=5, hidden_size=3, output_size=2, pop_size=20, generations=10, cx_prob=0.5, mut_prob=0.2):
    toolbox = setup_deap(input_size, hidden_size, output_size, pop_size, cx_prob, mut_prob)
    pop = toolbox.population(n=pop_size)

    # Evaluate the entire population
    fitnesses = list(map(toolbox.evaluate, pop))
    for ind, fit in zip(pop, fitnesses):
        ind.fitness.values = fit

    for gen in range(generations):
        # Selection
        offspring = toolbox.select(pop, len(pop))
        offspring = list(map(toolbox.clone, offspring))

        # Crossover
        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < cx_prob:
                toolbox.mate(child1, child2)
                del child1.fitness.values
                del child2.fitness.values
        
        # Mutation
        for mutant in offspring:
            if random.random() < mut_prob:
                toolbox.mutate(mutant)
                del mutant.fitness.values
        
        # Re-evaluate fitness of new individuals
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit

        # Replace population
        pop[:] = offspring

        # Optionally, print best fitness
        best_ind = tools.selBest(pop, 1)[0]
        print(f"Gen {gen+1} best fitness: {best_ind.fitness.values[0]:.3f}")

    # Return best overall
    best_ind = tools.selBest(pop, 1)[0]
    return best_ind, best_ind.fitness.values[0]
