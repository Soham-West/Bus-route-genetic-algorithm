from bus_grid_env import *

print(x_cords)
print(y_cords)

graph = {
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
        }

def bfs(graph, start, end):
    queue = []
    queue.append([start])
    while queue:
        path = queue.pop(0)
        node = path[-1]
        # path found
        if node == end:
            return path
        for adjacent in graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)

print(bfs(graph, "A", "Y"))