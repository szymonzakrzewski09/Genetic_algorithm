from utils_gen import *
from settings_gen import *

population = create_random_population()
describe_population(population)

for _ in range(how_much_repeat):
    new_population = []

    for _ in range(chromosome_count - 1):
        new_population.append(tournament_selected(population, tournament_size))

    new_population = mutation(new_population)

    new_population.append(return_best_member(population))

    describe_population(new_population)

    population = new_population

print('x1 = ', decoding(return_best_member(population)[0]), 'x2 = ', decoding(return_best_member(population)[1]))

print(decoding([1, 1, 1, 1, 1, 1, 1, 1, 1]))
print(decoding([0, 0, 0, 0, 0, 0, 0, 0, 0]))
