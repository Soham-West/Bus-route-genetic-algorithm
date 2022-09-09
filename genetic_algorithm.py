from branch_and_bound_algorithm import *

num_of_generations = 5
gen_size = 5
generation_population = []
best_route, best_score = annotations_2, 10
print(best_route)
print(best_score)
for x in range(gen_size - 1):
    population = random.sample(annotations_2, num_of_stops)
    print(population[x])
    generation_population.append(population.remove())

for gen in range(num_of_generations):
    continue
    #scores = [time(gen) for gen in generation_population]
print(population)
print(generation_population)