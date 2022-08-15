import matplotlib.pyplot as plt
import numpy as np
import random
import matplotlib.patches as mp
#Create 4 by 4 grid

# Sets number of stops and the size of grid
num_of_stops = 4
num_of_gridlines = 4

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
for i in range(1, num_of_gridlines + 2):
    traffic_cond_x = random.randint(1, 3)
    if traffic_cond_x == 1:
        plt.axhline(y = i - 1, xmin = 0, xmax = num_of_stops, c = "g", linewidth = 5.5)
    elif traffic_cond_x == 2:
        plt.axhline(y = i - 1, xmin = 0, xmax = num_of_stops, c = "y", linewidth = 5.5)
    elif traffic_cond_x == 3:
         plt.axhline(y = i - 1, xmin = 0, xmax = num_of_stops, c = "r", linewidth = 5.5)

# Sets the traffic conditions for the y coordinate
for i in range(1, num_of_stops + 2):
    traffic_cond_y = random.randint(1, 3)
    if traffic_cond_y == 1:
        plt.axvline(x = i - 1, ymin = 0, ymax = num_of_stops, c = "g", linewidth = 5.5)
    elif traffic_cond_y == 2:
        plt.axvline(x = i - 1, ymin = 0, ymax = num_of_stops, c = "y", linewidth = 5.5)
    elif traffic_cond_y == 3:
         plt.axvline(x = i - 1, ymin = 0, ymax = num_of_stops, c = "r", linewidth = 5.5)
         
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

# Prints the x coordinates and y coordinates for the branch and bound algorithm
for x_cord, y_cord in zip(x, y):
    print(x_cord, y_cord)

# Sets the axis for the grid       
axis = np.array([0, 4, 0 ,4])
plt.axis(axis)
   
# Sets x and y ticks to the number of gridlines
plt.xticks(range(0, num_of_gridlines))
plt.yticks(range(0, num_of_gridlines))

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
plt.show()