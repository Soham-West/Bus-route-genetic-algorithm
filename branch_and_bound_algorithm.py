from bus_grid_env import *
import math
# Makes the graph the bfs algorithm traverses through
def make_matrix(len_of_side):
    len_of_side = ((num_of_gridlines + 1)**2)
    graph = {}
    for i in range(1, len_of_side + 1):
        if i == 1:
            graph[str(i)] = [[str(i + 1), int(x_traffic[0])], [str(i + num_of_gridlines + 1), int(y_traffic[0])]]
        elif i == num_of_gridlines + 1:
            graph[str(i)] = [[str(i - 1), int(x_traffic[i - 2])], [str(i + num_of_gridlines + 1), int(y_traffic[i - 1])]]
        elif i == len_of_side - num_of_gridlines:
            graph[str(i)] = [[str(i - (num_of_gridlines + 1)), int(y_traffic[i - (num_of_gridlines + 2)])], [str(i + 1), int(x_traffic[i - (num_of_gridlines + 1)])]]
        elif i == len_of_side:
            graph[str(i)] = [[str(i - (num_of_gridlines + 1)), int(y_traffic[-1])], [str(i - 1), int(x_traffic[-1])]]
        elif 1 < i < num_of_gridlines + 1:
            graph[str(i)] = [[str(i - 1), int(x_traffic[i - 2])], [str(i + 1), int(x_traffic[i - 1])], [str(i + num_of_gridlines + 1), int(y_traffic[i - 1])]]
        elif (i - 1)%(num_of_gridlines + 1) == 0:
            num_of_iters = 0
            graph[str(i)] = [[str(i - (num_of_gridlines + 1)), int(y_traffic[i - (num_of_gridlines + 2)])], [str(i + 1), int(x_traffic[(i - 2 - num_of_iters)])], [str(i + num_of_gridlines + 1), int(y_traffic[i - 1])]]
            num_of_iters += 1
        elif i%(num_of_gridlines + 1) == 0:
            num_of_iters_0 = 0
            graph[str(i)] = [[str(i - (num_of_gridlines + 1)), int(y_traffic[i - (num_of_gridlines + 2)])], [str(i - 1), int(x_traffic[i - 3 - num_of_iters_0])], [str(i + num_of_gridlines + 1), int(y_traffic[i - 1])]]
            num_of_iters_0 += 1
        elif (len_of_side - num_of_gridlines) < i < len_of_side:
            graph[str(i)] = [[str(i - (num_of_gridlines + 1)), int(y_traffic[i - (num_of_gridlines + 2)])], [str(i - 1), int(x_traffic[i - (num_of_gridlines + 2)])], [str(i + 1), int(x_traffic[i - (num_of_gridlines + 1)])]]
        else:
            k = math.floor(i/(num_of_gridlines + 1))
            graph[str(i)] = [[str(i - (num_of_gridlines + 1)), int(y_traffic[i - (num_of_gridlines + 2)])], [str(i - 1), int(x_traffic[i - k - 2])], [str(i + 1), int(x_traffic[i - k - 1])], [str(i + num_of_gridlines + 1), int(y_traffic[i - 1])]]
        #graph[i] = [i]
    return graph   
# Gets the nearest starting node from the start point
def get_nearest_node(point1_x, point1_y, point2_x, point2_y):
    x_1 = float(point1_x)
    x_2 = float(point2_x)
    y_1 = float(point1_y)
    y_2 = float(point2_y)
    s_path = []
    if y_1.is_integer() == True and x_2 > x_1:
        s_path.append("R")
        t = math.floor(int(x_1) + 1.0)
        z = [t, int(y_1)]
    elif y_1.is_integer() == True and x_2 < x_1:
        s_path.append("L")
        t = math.ceil(int(x_1) - 1.0)
        z = [t, int(y_1)]
    elif x_1.is_integer() == True and y_2 > y_1:
        s_path.append("U")
        t = math.floor(y_1 + 1.0)
        z = [int(x_1), t]
    elif x_1.is_integer() == True and y_2 < y_1:
        s_path.append("D")
        t = math.ceil(y_1 - 1.0)
        z = [int(x_1), t]
    else:
        s_path.append("Start")
    pp = 1
    p1_x = z[0]
    p1_y = (num_of_gridlines - z[1]) * (num_of_gridlines + 1)
    group = p1_x + p1_y
    pp += group
    return [str(pp), s_path]
# Gets the nearest end node from the end point
def end_node(p1x, p1y, p2x, p2y):
    x_1 = float(p1x)
    x_2 = float(p2x)
    y_1 = float(p1y)
    y_2 = float(p2y)
    l_path = []
    if y_1.is_integer() == True and x_2 > x_1:
        t = math.floor(int(x_1) + 1.0)
        z = [t, int(y_1)]
    elif y_1.is_integer() == True and x_2 < x_1:
        t = math.ceil(int(x_1) - 1.0)
        z = [t, int(y_1)]
    elif x_1.is_integer() == True and y_2 > y_1:
        t = math.floor(y_1 + 1.0)
        z = [int(x_1), t]
    elif x_1.is_integer() == True and y_2 < y_1:
        t = math.ceil(y_1 - 1.0)
        z = [int(x_1), t]
    n = 1
    p1_x = z[0]
    p1_y = (num_of_gridlines - z[1]) * (num_of_gridlines + 1)
    group = p1_x + p1_y
    n += group
    if z[0] < p1x and z[1] == p1y:
        l_path.append("R")
    elif z[0] > p1x and z[1] == p1y:
        l_path.append("L")
    elif z[1] < p1y and z[0] == p1x:
        l_path.append("U")
    elif z[1] < p1y and z[0] == p1x:
        l_path.append("D")
    else:
        l_path.append("Finish")
    return [str(n), l_path]
#Breadth First algorithm
def bfs(graph, start, end):
    shortest_distance = {}
    pred = {}
    unseen_N = graph
    inf = 123456789
    track_path = []
    for node in unseen_N:
        shortest_distance[node] = inf
    shortest_distance[start] = 0
    while unseen_N:
        min_distance = None
        for node in unseen_N:
            if min_distance is None:
                min_distance = node
            elif shortest_distance[node] < shortest_distance[min_distance]:
                min_distance = node
        options = graph.get(str(min_distance))
        for c_node, weight in options:
            if weight + shortest_distance[min_distance] < shortest_distance[c_node]:
                shortest_distance[c_node] = weight + shortest_distance[min_distance]
                pred[c_node] = min_distance
        unseen_N.pop(min_distance)
    current_N = end

    while current_N != start:
        try:
            track_path.insert(0, current_N)
            current_N = pred[current_N]
        except KeyError:
            print("Starting Point and End Point are the same") 
            break
    track_path.insert(0, start)

    if shortest_distance[end] != inf:
        #print(shortest_distance[end])
        #print(path)
        return [track_path, shortest_distance[end]]

def nodes_to_cords(node):
    node0 = int(node)
    x = math.floor((node0 % (num_of_gridlines + 1)) - 1)
    y_k = math.floor(node0/(num_of_gridlines + 1))
    y = num_of_gridlines - y_k
    if node0 % (num_of_gridlines + 1) == 0:
        x = num_of_gridlines
        y_k = (node0/(num_of_gridlines + 1)) - 1
        y = num_of_gridlines - y_k
    return [x, y]
#print(nodes_to_cords("6"))
def fastest_2_points(point1, point2):
    if point1 == "School":
        point1x = x_cords[0]
        point1y = y_cords[0]    
        s = ord(point2) - 64
        point2x = x_cords[s]
        point2y = y_cords[s]
    elif point2 == "School":
        k = ord(point1) - 64
        point1x = x_cords[k]
        point1y = y_cords[k]
        point2x = x_cords[0]
        point2y = y_cords[0]
    else:
        k = ord(point1) - 64
        s = ord(point2) - 64
        point1x = x_cords[k]
        point1y = y_cords[k]
        point2x = x_cords[s]
        point2y = y_cords[s]
    r_path = []
    r_path.append(get_nearest_node(point1x, point1y, point2x, point2y)[1][0])
    start_point = get_nearest_node(point1x, point1y, point2x, point2y)[0]
    end_point = end_node(point2x, point2y, point1x, point1y)[0]
    graph = make_matrix(num_of_gridlines)
    path = bfs(graph, start_point, end_point)[0]
    graph = make_matrix(num_of_gridlines)
    shortest_d = bfs(graph, start_point, end_point)[1]
    for direction in range(0, (len(path)) - 1):
        if int(path[direction]) + 1 == int(path[direction + 1]):
            r_path.append("R")
        elif int(path[direction]) - (num_of_gridlines + 1) == int(path[direction + 1]):
            r_path.append("U")
        elif int(path[direction]) - 1 == int(path[direction + 1]):
            r_path.append("L")
        elif int(path[direction]) + (num_of_gridlines + 1) == int(path[direction + 1]):
            r_path.append("D")
    graph = make_matrix(num_of_gridlines)
    r_path.append(end_node(point2x, point2y, point1x, point1y)[1][0])
    point1_movement = ((point1x % 1) + (point1y % 1)) * 2
    point2_movement = ((point2x % 1) + (point2y % 1)) * 2
    point_movement = point1_movement + point2_movement
    shortest_d += round(point_movement, 1)
    return [shortest_d, path, r_path, point1x, point1y, point2x, point2y]

def draw_graph(path, point1x, point1y, point2x, point2y):
    first_coord_x = nodes_to_cords(path[0])[0]
    first_coord_y = nodes_to_cords(path[0])[1]
    plt.plot([point1x, first_coord_x], [point1y, first_coord_y], "b--", lw = 6)
        #plt.plot[0]
    for i in range(0, len(path) - 1):
        x = nodes_to_cords(path[i])[0]
        y = nodes_to_cords(path[i])[1]
        x_1 = nodes_to_cords(path[i + 1])[0]
        y_1 = nodes_to_cords(path[i + 1])[1]
        plt.plot([x, x_1], [y, y_1], "b--", lw = 6)
    last_coord_x = nodes_to_cords(path[-1])[0]
    last_coord_y = nodes_to_cords(path[-1])[1]
    plt.plot([point2x, last_coord_x], [point2y, last_coord_y], "b--", lw = 6)
