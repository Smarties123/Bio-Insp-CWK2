"""
genetic_algorithm.py

Implements a simple genetic algorithm to evolve neural networks.
"""

import numpy as np
from .neural_net import SimpleNeuralNet

def evaluate_fitness(network: SimpleNeuralNet) -> float:
    """
    Example fitness function. 
    In a real scenario, you'd integrate with the Game of Life or some environment.
    For now, we do something arbitrary: e.g., measure how 'close' the output is to a target vector.
    """
    # Just a toy example: feed in random inputs and see how close output is to [1, -1] or something.
    total_score = 0.0
    for _ in range(5):
        x = np.random.randn(network.input_size)
        target = np.array([1.0, -1.0])
        out = network.forward(x)
        total_score += -np.sum((out - target)**2)  # negative MSE
    return total_score

def mutate(network: SimpleNeuralNet, mutation_rate=0.1):
    """
    Mutate the network weights/biases by adding small Gaussian noise 
    with probability 'mutation_rate'.
    """
    net = network.copy()
    # For each parameter, flip a coin to decide if we mutate it
    def maybe_mutate(array):
        mask = np.random.rand(*array.shape) < mutation_rate
        noise = np.random.randn(*array.shape) * 0.1
        array[mask] += noise[mask]
    
    maybe_mutate(net.weights_input_hidden)
    maybe_mutate(net.bias_hidden)
    maybe_mutate(net.weights_hidden_output)
    maybe_mutate(net.bias_output)
    
    return net

def crossover(parent1: SimpleNeuralNet, parent2: SimpleNeuralNet) -> SimpleNeuralNet:
    """
    One-point crossover for demonstration. 
    We'll just do it on the hidden-output weights for simplicity. 
    In practice, you'd do a more thorough crossover.
    """
    child = parent1.copy()
    # Flatten the arrays for a simple demonstration
    w1 = parent1.weights_hidden_output.flatten()
    w2 = parent2.weights_hidden_output.flatten()
    cross_point = np.random.randint(len(w1))
    w_child = np.concatenate([w1[:cross_point], w2[cross_point:]])
    # reshape back
    child.weights_hidden_output = w_child.reshape(child.hidden_size, child.output_size)
    return child

def select_parents(population, fitnesses, num_parents=2):
    """
    Simple tournament selection or rank-based. 
    We'll do a basic 'top K' selection for demonstration.
    """
    # Sort by fitness descending
    sorted_pop = sorted(zip(population, fitnesses), key=lambda x: x[1], reverse=True)
    parents = [p for (p, fit) in sorted_pop[:num_parents]]
    return parents

def run_ga(pop_size=20, generations=10, input_size=5, hidden_size=3, output_size=2):
    """
    Run the genetic algorithm for a number of generations,
    return the best network found and its fitness.
    """
    # 1. Initialize population
    population = [
        SimpleNeuralNet(input_size, hidden_size, output_size) 
        for _ in range(pop_size)
    ]
    
    best_net = None
    best_fitness = -1e9
    
    # GA Loop
    for gen in range(generations):
        # Evaluate fitness
        fitnesses = [evaluate_fitness(net) for net in population]
        
        # Track best
        gen_best_idx = np.argmax(fitnesses)
        if fitnesses[gen_best_idx] > best_fitness:
            best_fitness = fitnesses[gen_best_idx]
            best_net = population[gen_best_idx].copy()
        
        # Selection
        parents = select_parents(population, fitnesses, num_parents=2)
        
        # Reproduction
        new_population = []
        for _ in range(pop_size):
            # pick two parents
            p1, p2 = np.random.choice(parents, 2)
            child = crossover(p1, p2)
            child = mutate(child, mutation_rate=0.2)
            new_population.append(child)
        
        population = new_population
    
    return best_net, best_fitness
