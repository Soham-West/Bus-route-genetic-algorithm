from branch_and_bound_algorithm import *

def time(gen):
    distance = 0
    for i in range(0, (len(gen) - 1)):
        distance += (fastest_2_points(gen[i], gen[i + 1])[0])
    return distance
#time(["A", "B", "C", "D"])

num_of_generations = 10
gen_size = 10
generation_population = []
best_route, best_score = annotations_2, 100
for x in range(gen_size):
    population = random.sample(annotations_2, num_of_stops)
    generation_population.append(population)
    


for gen in range(num_of_generations):

    scores = [time(gen) for gen in generation_population]
    for i in range(gen_size):
        if scores[i] < best_score:
            best_route, best_score = generation_population[i], scores[i]


    parent = best_route
    children = []

    children.append(parent)

    for i in range(1, gen_size):
        child = random.sample(annotations_2, num_of_stops)
        children.append(child)

    generation_population = children
print(best_route)
print(best_score)
for i in range(0, len(best_route) - 1):
    print(fastest_2_points(best_route[i], best_route[i + 1])[2])

#draw_graph(path, [])
#print(generation_population)
#plt.show()
