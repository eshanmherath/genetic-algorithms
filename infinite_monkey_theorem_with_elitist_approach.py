"""
This implements a GA approach to infinite monkey theorem problems.
The GA focus on evolving it self to come up with the correct sequence of words to match the phrase given at beginning.
Both genotype and phenotype are similar in this scenario (DNA is the sequence of characters)
"""

from random import choice, randint


def fitness(current_phrase):
    """match the phrase with the original phrase and return how many characters match. this is the fitness"""
    global original_phrase
    return sum(a == b for a, b in zip(original_phrase, current_phrase))


original_phrase = "superman is from krypton"
population_size = 100
mutation_rate = 0.01
max_generations = 1000
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', ' ']

phrase_length = len(original_phrase)

"""fill the initial population with parses of random character sequences"""
population = {}

for i in range(population_size):
    phrase_dna = []
    for character_position in range(phrase_length):
        phrase_dna.append(choice(alphabet))
    phrase = ''.join(phrase_dna)
    population[i] = phrase

generation = 0
while generation <= max_generations:
    generation += 1
    """calculate fitness"""
    fitness_scores = []
    for i in range(population_size):
        fitness_score = fitness(population[i])
        if fitness_score == phrase_length:
            print("\n\nGenetic Algorithm Completed. Match Found")
            print("Expected phrase : " + original_phrase)
            print("GA phrase       : " + population[i])
            exit()
        else:
            fitness_scores.append(fitness_score)

    """normalize fitness"""
    total_score = sum(fitness_scores)
    fitness_scores = [score * 100 / total_score for score in fitness_scores]

    """elitist based selection"""
    population_selection_index = {}
    for i in range(population_size):
        population_selection_index[i] = fitness_scores[i]
    population_selection_index = sorted(population_selection_index.items(), key=lambda x: x[1], reverse=True)

    top_candidate = population_selection_index[0][0]
    print("Generation : " + str(generation) + "\t\t" + str(population[top_candidate]))

    parent_candidates = []
    for candidate in population_selection_index:
        parent_candidates.append(population[candidate[0]])

    selected_parents = parent_candidates[:int(population_size / 2)]

    """crossover"""
    mid_point = int(phrase_length / 2) if phrase_length % 2 == 0 else int(phrase_length + 1) / 2

    new_generation = []
    for rank in range(len(selected_parents)):
        parent_1 = selected_parents[rank]
        if rank == len(selected_parents):
            parent_2 = selected_parents[rank + 1]
        else:
            parent_2 = selected_parents[0]
        child_1 = parent_1[:mid_point] + parent_2[mid_point:]
        child_2 = parent_2[:mid_point] + parent_1[mid_point:]
        new_generation.append(child_1)
        new_generation.append(child_2)

    """mutation"""
    mutated_generation = []
    for child in new_generation:
        child_dna = list(child)
        for i in range(len(child)):
            random_value = randint(0, 99)
            if random_value <= mutation_rate * 100:
                child_dna[i] = choice(alphabet)
        mutated_child = ''.join(child_dna)
        mutated_generation.append(mutated_child)

    population = mutated_generation
