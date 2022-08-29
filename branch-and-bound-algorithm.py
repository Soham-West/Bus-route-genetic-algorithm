from bus_grid_env import *
print(((num_of_gridlines + 1)**2) - num_of_gridlines)
##print(y_cords)
def make_matrix(len_of_side):
    len_of_side = ((num_of_gridlines + 1)**2)
    graph = {}
    for i in range(1, len_of_side + 1):
        if i == 1:
            graph[i] = [i + 1, i + num_of_gridlines + 1]
        elif i == num_of_gridlines + 1:
            graph[i] = [i - 1, i + num_of_gridlines + 1]
        elif i == len_of_side - num_of_gridlines:
            graph[i] = [i - (num_of_gridlines + 1), i + 1]
        elif i == len_of_side:
            graph[i] = [i - (num_of_gridlines + 1), i - 1]
        elif 1 < i < num_of_gridlines + 1:
            graph[i] = [i - 1, i + 1, i + num_of_gridlines + 1]
        elif (i - 1)%(num_of_gridlines + 1) == 0:
            graph[i] = [i - (num_of_gridlines + 1), i + 1, i + num_of_gridlines + 1]
        elif i%(num_of_gridlines + 1) == 0:
            graph[i] = [i - (num_of_gridlines + 1), i - 1, i + num_of_gridlines + 1]
        elif (len_of_side - num_of_gridlines) < i < len_of_side:
            graph[i] = [i + num_of_gridlines + 1, i - 1, i + 1]
        else:
            graph[i] = [i - (num_of_gridlines + 1), i - 1, i + 1, i + num_of_gridlines + 1]
        


    #graph[i] = [i]
    print(graph)
graph = make_matrix(num_of_gridlines)
"""graph = {
        "A": ["B", "F"],
        "B": ["A", "C", "G"],
        "C": ["B", "D", "H"],
        "D": ["C", "E", "I"],
        "E": ["D", "J"],
        "F": ["A", "G", "K"],
        "G": ["B", "F", "H", "L"],
        "H": ["C", "G", "I", "M"],
        "I": ["D", "H", "J", "N"],
        "J": ["E", "I", "O"],
        "K": ["F", "L", "P"],
        "L": ["G", "K", "M", "Q"],
        "M": ["H", "L", "N", "R"],
        "N": ["I", "M", "O", "S"],
        "O": ["J", "N", "T"],
        "P": ["K", "Q", "U"],
        "Q": ["L", "P", "R", "V"],
        "R": ["M", "Q", "S", "W"],
        "S": ["N", "R", "T", "X"],
        "T": ["O", "S", "Y"],
        "U": ["P", "V"],
        "V": ["Q", "U", "W"],
        "W": ["R", "X"],
        "X": ["S", "W", "Y"],
        "Y": ["T", "X"]
        }"""

def bfs(graph, start, end):
    queue = []
    queue.append([start])
    while queue:
        path = queue.pop(0)
        node = path[-1]
        # path found
        if node == end:
            return path
        print(graph.get(node, []))
        for adjacent in graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)
        for direction in "U", "R", "D", "L":
            branch = object()


  
#print(bfs(graph, "A", "Y"))

