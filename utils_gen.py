import random
from statistics import mean
import math
from settings_gen import chromosome_count, chromosome_length, x_min, x_max
import copy

def create_random_population(count: int = chromosome_count, length: int = chromosome_length):
    start_population = []

    for amount_list in range(0, count):
        chromosome_values = []


        for x in range(2):
            chromosome = []


            for length_list in range(0, length):
                chromosome.append(random.randint(0, 1))

            chromosome_values.append(chromosome)

        start_population.append(chromosome_values)

    return start_population


def adaptive_function(x1, x2):

    return math.sin(x1 * 0.05) + math.sin(x2 * 0.05) + 0.4 * math.sin(x1 * 0.15) * math.sin(x2 * 0.15)


def decoding(tab: list, x_min: int = x_min, x_max: int = x_max) -> float:
    length_tab = len(tab)
    number_binary = "".join(str(bit) for bit in tab)
    number_decimal = int(number_binary, 2)

    coded_value = x_min + (x_max - x_min) * (
                number_decimal / (2 ** length_tab - 1))
    return coded_value


def index_of_max_value(list_of_values):
    max_value = max(list_of_values)
    max_index = list_of_values.index(max_value)
    return max_index


def return_best_member(population: list = None):
    list_values_adaptive_function = []
    for character in population:
        x_1 = decoding(character[0])
        x_2 = decoding(character[1])
        list_values_adaptive_function.append(
            adaptive_function(x_1, x_2))
    return population[index_of_max_value(
        list_values_adaptive_function)]


def describe_population(population: list = None):
    list_values_adaptive_function = []

    for character in population:
        x_1 = decoding(character[0])
        x_2 = decoding(character[1])
        list_values_adaptive_function.append(adaptive_function(x_1, x_2))

    print('Max', max(list_values_adaptive_function))
    print('Mean: ', mean(list_values_adaptive_function), '\n')


def crossover_help(pop1: list, pop2: list, point: int) -> tuple[list[int], list[int]]:
    parent1 = list(''.join(str(_) for _ in pop1))
    parent2 = list(''.join(str(_) for _ in pop2))

    for i in range(point, len(parent1)):
        parent1[i], parent2[i] = parent2[i], parent1[i]

    p1, p2 = ''.join(parent1), ''.join(parent2)
    p1, p2 = [int(x) for x in p1], [int(x) for x in p2]

    return p1, p2


def main_crossover_population(population, first_pop_index, second_pop_index, mutation_point):
    segregation_list_population = []

    for x in range(2):
        segregation_list_population.append(
            crossover_help(population[first_pop_index][x], population[second_pop_index][x],mutation_point))

    first_person, second_person = [], []

    first_person.append(segregation_list_population[0][0])
    first_person.append(segregation_list_population[1][0])
    second_person.append(segregation_list_population[0][1])
    second_person.append(segregation_list_population[1][1])

    return first_person, second_person


def tournament_selected(pop, size_tournament):
    selected_person = []

    for _ in range(size_tournament):
        selected_person.append(random.choice(pop))

    selected_person.sort(key=evaluation_person, reverse=True)

    return selected_person[0]


def evaluation_person(person):
    x_1 = decoding(person[0])
    x_2 = decoding(person[1])
    return adaptive_function(x_1, x_2)


def mutation(pop):
    mutated_list = []

    for person in pop:
        new_person = copy.deepcopy(person)
        index_gen = random.randint(0, len(person[0]) - 1)
        rand = random.randint(0, 1)
        new_person[rand][index_gen] = 1 - new_person[rand][index_gen]
        mutated_list.append(new_person)

    return mutated_list