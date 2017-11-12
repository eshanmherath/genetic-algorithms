"""
This implements different possible fitness functions for the solution to the infinite monkey problem with GA approach
"""

original_phrase = 'superman is from krypton'


def fitness_1(current_phrase):
    """
    match the phrase with the original phrase and return how many characters match. this is the fitness.
    fitness of a phrase matching 10 characters and fitness of a phrase matching 11 characters are given close chances
    """
    global original_phrase
    return sum(a == b for a, b in zip(original_phrase, current_phrase))


def fitness_2(current_phrase):
    """
    match the phrase with the original phrase and return how many characters match. this is the fitness
    fitness of a phrase matching 10 characters is given a less value than the
    fitness of a phrase matching 11 characters
    """
    global original_phrase
    matches = sum(a == b for a, b in zip(original_phrase, current_phrase))
    return matches*matches


def fitness_3(current_phrase):
    """
    match the phrase with the original phrase and return how many characters match. this is the fitness
    fitness of a phrase matching 10 characters is given a much less value than the
    fitness of a phrase matching 11 characters
    """
    global original_phrase
    matches = sum(a == b for a, b in zip(original_phrase, current_phrase))
    return 2**matches

print('\nfitness_1')
f1_a = fitness_1('superman is from crypten')
f1_b = fitness_1('superman is from krypten')
total_f1 = f1_a + f1_b
f1_a = f1_a/total_f1
f1_b = f1_b/total_f1
print(f1_a)
print(f1_b)

print('\nfitness_2')
f2_a = fitness_2('superman is from crypten')
f2_b = fitness_2('superman is from krypten')
total_f2 = f2_a + f2_b
f2_a = f2_a/total_f2
f2_b = f2_b/total_f2
print(f2_a)
print(f2_b)

print('\nfitness_3')
f3_a = fitness_3('superman is from crypten')
f3_b = fitness_3('superman is from krypten')
total_f3 = f3_a + f3_b
f3_a = f3_a/total_f3
f3_b = f3_b/total_f3
print(f3_a)
print(f3_b)