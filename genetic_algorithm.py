from branch_and_bound_algorithm import *

def time(gen):
    distance = 0
    for i in range(0, (len(gen) - 1)):
        distance += (fastest_2_points(gen[i], gen[i + 1])[0])
    return distance
#time(["A", "B", "C", "D"])

def mutate(gen):
    change_index_1 = random.randint(1, len(gen) - 2)
    change_index_2 = random.randint(1, len(gen) - 2)
    if change_index_1 == change_index_2:
        change_index_2 = random.randint(1, len(gen) - 2)
    stop_1 = gen[change_index_1]
    stop_2 = gen[change_index_2]
    gen[change_index_2] = stop_1
    gen[change_index_1] = stop_2
    return gen

num_of_generations = 7
gen_size = 7
generation_population = []
best_route, best_score = annotations_2, 1000000
for x in range(gen_size):
    population_0 = random.sample(annotations_2, num_of_stops)
    population = ["School"] + population_0 + ["School"]
    generation_population.append(population)
    


for gen in range(num_of_generations):

    scores = [time(gen) for gen in generation_population]
    for i in range(gen_size):
        if scores[i] < best_score:
            best_route, best_score = generation_population[i], scores[i]


    parent = best_route
    children = []

    children.append(parent)
    child_1 = mutate(parent)
    child_2 = mutate(parent)
    children.append(child_1)
    children.append(child_2)
    for i in range(3, gen_size):
        child_0 = random.sample(annotations_2, num_of_stops)
        child = ["School"] + child_0 + ["School"]
        children.append(child)

    generation_population = children
print(best_route)
print(best_score)
for i in range(0, len(best_route) - 1):
    point1x = fastest_2_points(best_route[i], best_route[i + 1])[3]
    point1y = fastest_2_points(best_route[i], best_route[i + 1])[4]
    point2x = fastest_2_points(best_route[i], best_route[i + 1])[5]
    point2y = fastest_2_points(best_route[i], best_route[i + 1])[6]
    path = fastest_2_points(best_route[i], best_route[i + 1])[1]
    draw_graph(path, point1x, point1y, point2x, point2y)

#draw_graph(path, [])
#print(generation_population)
plt.show()
