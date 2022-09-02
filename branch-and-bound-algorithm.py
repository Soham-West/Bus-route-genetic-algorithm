from bus_grid_env import *
import math
#print(((num_of_gridlines + 1)**2) - num_of_gridlines)
##print(y_cords)
def make_matrix(len_of_side):
    len_of_side = ((num_of_gridlines + 1)**2)
    graph = {}
    for i in range(1, len_of_side + 1):
        if i == 1:
            graph[str(i)] = [str(i + 1), str(i + num_of_gridlines + 1)]
        elif i == num_of_gridlines + 1:
            graph[str(i)] = [str(i - 1), str(i + num_of_gridlines + 1)]
        elif i == len_of_side - num_of_gridlines:
            graph[str(i)] = [str(i - (num_of_gridlines + 1)), str(i + 1)]
        elif i == len_of_side:
            graph[str(i)] = [str(i - (num_of_gridlines + 1)), str(i - 1)]
        elif 1 < i < num_of_gridlines + 1:
            graph[str(i)] = [str(i - 1), str(i + 1), str(i + num_of_gridlines + 1)]
        elif (i - 1)%(num_of_gridlines + 1) == 0:
            graph[str(i)] = [str(i - (num_of_gridlines + 1)), str(i + 1), str(i + num_of_gridlines + 1)]
        elif i%(num_of_gridlines + 1) == 0:
            graph[str(i)] = [str(i - (num_of_gridlines + 1)), str(i - 1), str(i + num_of_gridlines + 1)]
        elif (len_of_side - num_of_gridlines) < i < len_of_side:
            graph[str(i)] = [str(i + num_of_gridlines + 1), str(i - 1), str(i + 1)]
        else:
            graph[str(i)] = [str(i - (num_of_gridlines + 1)), str(i - 1), str(i + 1), str(i + num_of_gridlines + 1)]
        #graph[i] = [i]
    
    return graph   
        

graph = make_matrix(num_of_gridlines)
#print(graph)
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
s_path = []
def get_nearest_node(point1_x, point1_y, point2_x, point2_y):
    x_1 = float(point1_x)
    x_2 = float(point2_x)
    y_1 = float(point1_y)
    y_2 = float(point2_y)
    if y_1.is_integer() == True and x_2 > x_1:
        s_path.append("R")
        t = math.floor(x_1 + 1.0)
        z = [t, y_1]
        print(z)
    elif y_1.is_integer() == True and x_2 < x_1:
        s_path.append("L")
        t = math.ceil(x_1 - 1.0)

    elif x_1.is_integer() == True and y_2 > y_1:
        s_path.append("U")
    elif x_1.is_integer() == True and y_2 < y_1:
        s_path.append("D")
    print(s_path)
    
get_nearest_node(x_cords[0], y_cords[0], x_cords[1], y_cords[1])
print(used_annotations[0], used_annotations[1])
plt.show()


def bfs(graph, p_start, p_end):
    queue = []
    queue.append([p_start])
    visited = set()
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node in visited:
            continue
        if node == p_end:
            #print(len(path))
            r_path = []
            for direction in range(1, (len(new_path) - 1)):
                if int(new_path[direction]) + 1 == int(new_path[direction + 1]):
                    r_path.append("R")
                if int(new_path[direction]) + num_of_gridlines + 1 == int(new_path[direction + 1]):
                    r_path.append("D")
                if int(new_path[direction]) - 1 == int(new_path[direction + 1]):
                    r_path.append("L")
                if int(new_path[direction]) - (num_of_gridlines + 1) == int(new_path[direction + 1]):
                    r_path.append("U")

            print(r_path)
            return path
        else:
            for adjacent in graph.get(node, []):
                if adjacent not in visited:
                    new_path = list(path)
                    new_path.append(adjacent)
                    queue.append(new_path)
          

        


  
print(bfs(graph, "1", "13"))

