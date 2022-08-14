import matplotlib.pyplot as plt
import numpy as np
import random
import matplotlib.patches as mp
#Create 4 by 4 grid
num_of_stops = 4
x = []
y = []
for s in range(0, num_of_stops + 1):
    o = random.uniform(0, num_of_stops)
    h = random.uniform(0, num_of_stops)
    if (o.is_integer() is False) and (h.is_integer() is False):
        if o > num_of_stops/2:
            o = random.randint(0, num_of_stops)
        elif o <= num_of_stops/2:
            h = random.randint(0, num_of_stops)
        
    x.append(o)
    y.append(h)

annotations = ["School", "A", "B", "C", "D"]
used_annotations = random.sample(annotations, len(annotations))

line1 = plt.plot([x], [y], "--bo", markersize = 8)
l = line1.pop(0)
l.remove()

for a, label in enumerate(used_annotations):
    plt.text(x[a], y[a], used_annotations[a], fontweight = "bold")


for x_cord, y_cord in zip(x, y):
   # print(x_cord, y_cord)
   continue
        
axis = np.array([0, 4, 0 ,4])
plt.axis(axis)

for i in range(1, num_of_stops + 2):
    traffic_cond_x = random.randint(1, 3)
    if traffic_cond_x == 1:
        plt.axhline(y = i - 1, xmin = 0, xmax = num_of_stops, c = "g", linewidth = 5.5)
    elif traffic_cond_x == 2:
        plt.axhline(y = i - 1, xmin = 0, xmax = num_of_stops, c = "y", linewidth = 5.5)
    elif traffic_cond_x == 3:
         plt.axhline(y = i - 1, xmin = 0, xmax = num_of_stops, c = "r", linewidth = 5.5)

for i in range(1, num_of_stops + 2):
    traffic_cond_y = random.randint(1, 3)
    if traffic_cond_y == 1:
        plt.axvline(x = i - 1, ymin = 0, ymax = num_of_stops, c = "g", linewidth = 5.5)
    elif traffic_cond_y == 2:
        plt.axvline(x = i - 1, ymin = 0, ymax = num_of_stops, c = "y", linewidth = 5.5)
    elif traffic_cond_y == 3:
         plt.axvline(x = i - 1, ymin = 0, ymax = num_of_stops, c = "r", linewidth = 5.5)
   

plt.xticks(range(0, num_of_stops))
plt.yticks(range(0, num_of_stops))

green_traffic = mp.Patch(color = "green", label = "Low Traffic")
yellow_traffic = mp.Patch(color = "yellow", label = "Medium Traffic")
red_traffic = mp.Patch(color = "red", label = "High Traffic")

plt.xlabel("Latitude")
plt.ylabel("Longitude")

plt.tight_layout()
plt.grid()
plt.legend(handles = [green_traffic, yellow_traffic, red_traffic], prop = {"size": 8.5})
plt.show()