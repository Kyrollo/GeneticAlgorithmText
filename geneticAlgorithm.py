import random

POP_SIZE = 500
MUT_RATE = 0.1
TARGET = 'cognitive science'
GENES = ' abcdefghijklmnopqrstuvwxyz'

def initialize_pop(target):
    population = []
    for _ in range(POP_SIZE):
        chromosome = ''.join(random.choices(GENES, k=len(target)))
        population.append(chromosome)
    return population

def fitness_cal(target, chromosome):
    difference = sum(1 for t, c in zip(target, chromosome) if t != c)
    return difference

def selection(population, target):
    sorted_population = sorted(population, key=lambda x: fitness_cal(target, x))
    return sorted_population[:int(0.5*POP_SIZE)]

def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def mutation(chromosome):
    mutated_chromosome = list(chromosome)
    for i in range(len(mutated_chromosome)):
        if random.random() < MUT_RATE:
            mutated_chromosome[i] = random.choice(GENES)
    return ''.join(mutated_chromosome)

def replacement(selected_population, target):
    new_generation = []
    for _ in range(POP_SIZE):
        parent1, parent2 = random.choices(selected_population, k=2)
        child1, child2 = crossover(parent1, parent2)
        child1 = mutation(child1)
        child2 = mutation(child2)
        new_generation.extend([child1, child2])
    return new_generation

def main():
    population = initialize_pop(TARGET)
    generation = 1
    while True:
        selected_population = selection(population, TARGET)
        best_chromosome = selected_population[0]
        fitness = fitness_cal(TARGET, best_chromosome)
        if fitness == 0:
            print("Found the target in generation " + str(generation))
            break
        print("Generation " + str(generation) + ": " + best_chromosome)
        population = replacement(selected_population, TARGET)
        generation += 1

if __name__ == "__main__":
    main()
