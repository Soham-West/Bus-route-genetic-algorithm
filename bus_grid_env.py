import matplotlib.pyplot as plt
import numpy as np
import random
import matplotlib.patches as mp
#Create 4 by 4 grid

# Sets number of stops and the size of grid
num_of_stops = 4
num_of_gridlines = 50

# Sets x and y so that one integer and one float coordinate comes out. 
# Also sets the length of x and y to the number of stops
x = []
y = []
for s in range(0, num_of_stops + 1):
    o = random.uniform(0, num_of_gridlines)
    h = random.uniform(0, num_of_gridlines)
    if (o.is_integer() is False) and (h.is_integer() is False):
        if o > num_of_gridlines/2:
            o = random.randint(0, num_of_gridlines)
        elif o <= num_of_gridlines/2:
            h = random.randint(0, num_of_gridlines)
        
    x.append(o)
    y.append(h)


# Sets the traffic conditions for the x coordinate
lst = ["r", "y", "g"] * num_of_gridlines
x_traffic = []
def cycle_through_traffic_x(height, gridlines):
    x_lst = random.sample(lst, num_of_gridlines)
    for i in range(0, gridlines):
        plt.plot([i, i + 1], [height, height], c = x_lst[i], lw= 5.5)
        if x_lst[i] == "g":
            x_traffic.append("1")
        elif x_lst[i] == "y":
            x_traffic.append("2")
        elif x_lst[i] == "r":
            x_traffic.append("3")

lst = ["r", "y", "g"] * num_of_gridlines
y_traffic = []
def cycle_through_traffic_y(gridlines, decrease):
    y_lst = random.sample(lst, num_of_gridlines + 1)
    for i in range(0, gridlines + 1):
        plt.plot([i, i], [decrease , decrease - 1], c = y_lst[i], lw= 5.5)
        if y_lst[i] == "g":
            y_traffic.append("1")
        elif y_lst[i] == "y":
            y_traffic.append("2")
        elif y_lst[i] == "r":
            y_traffic.append("3")


# Sets the traffic conditions for the x coordinate
for x_t in reversed(range(0, num_of_gridlines + 1)):
    cycle_through_traffic_x(x_t, num_of_gridlines)
print(x_traffic)
# Sets the traffic conditions for the y coordinate
for y_t in reversed(range(1, num_of_gridlines + 1)):
    cycle_through_traffic_y(num_of_gridlines, y_t)
print(y_traffic)
#Creates the list with all of the stops name and school in random order
annotations_1 = ["School"]
annotations_2 = [chr(ord("@") + number) for number in range(1, num_of_stops + 1)]
annotations = annotations_1 + annotations_2
used_annotations = random.sample(annotations, len(annotations))

# Plots the line with x and y and sets ccolor to blue marks the points with a dot
# Also removes the line to remove extra color.
line1 = plt.plot([x], [y], "--bo", markersize = 8)
l = line1.pop(0)
l.remove()

# Enumerates used_annotations into numbers and then adds text to the points
for a, labels in enumerate(used_annotations):
    plt.text(x[a], y[a], used_annotations[a], fontweight = "bold")

x_cords = []
y_cords = []

# Prints the x coordinates and y coordinates for the branch and bound algorithm
for x_cord, y_cord in zip(x, y):
    print(x_cord, y_cord)
    x_cords.append(x_cord)
    y_cords.append(y_cord)

# Sets the axis for the grid       
axis = np.array([0, 4, 0 ,4])
plt.axis(axis)
   
# Sets x and y ticks to the number of gridlines
plt.xticks(range(0, num_of_gridlines + 1))
plt.yticks(range(0, num_of_gridlines + 1))

#Sets the legend
green_traffic = mp.Patch(color = "green", label = "Low Traffic")
yellow_traffic = mp.Patch(color = "yellow", label = "Medium Traffic")
red_traffic = mp.Patch(color = "red", label = "High Traffic")

plt.xlabel("Latitude")
plt.ylabel("Longitude")

# Formatting and plotting
plt.tight_layout()
plt.grid()
plt.legend(handles = [green_traffic, yellow_traffic, red_traffic], prop = {"size": 8.5})
#plt.show()
