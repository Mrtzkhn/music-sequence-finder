import numpy as np


class GeneticAlgorithm:
    def __init__(self, config):
        self.target = config["target_sequence"]
        self.population_size = config["population_size"]
        self.generations = config["generations"]
        self.mutation_rate = config["mutation_rate"]
        self.population = self.initialize_population()

    def initialize_population(self):
        """Generate initial population as random permutations of the target sequence."""
        return [np.random.permutation(self.target).tolist() for _ in range(self.population_size)]

    def roulette_selection(self, fitness_scores):
        """Select parents using roulette wheel selection."""
        total_fitness = sum(fitness_scores)
        probabilities = [f / total_fitness for f in fitness_scores]
        return np.random.choice(len(self.population), p=probabilities, size=2)  # returns index

    def crossover(self, parent1, parent2):
        """One-point crossover"""
        # Choose a random crossover point
        point = np.random.randint(1, len(self.target))

        # Take segments from parents
        child1 = parent1[:point]
        child2 = parent2[:point]

        # Fill the rest without exceeding the required length
        for x in parent2:
            if len(child1) < len(self.target) and child1.count(x) < parent1.count(x):
                child1.append(x)

        for x in parent1:
            if len(child2) < len(self.target) and child2.count(x) < parent2.count(x):
                child2.append(x)

        return child1, child2

    def mutate(self, sequence):
        """Apply mutation by swapping two random elements."""
        if np.random.rand() < self.mutation_rate:
            idx1, idx2 = np.random.choice(len(sequence), 2, replace=False)
            sequence[idx1], sequence[idx2] = sequence[idx2], sequence[idx1]

    @staticmethod
    def calculate_fitness(sequence, target):
        epsilon = 1e-10
        distance = sum(abs(a - b) for a, b in zip(sequence, target))
        fitness = 1 / (distance + epsilon)
        return fitness
