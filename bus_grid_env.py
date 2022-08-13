import matplotlib.pyplot as plt
import numpy as np
import random
from collections import Counter
import math
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
print(x)
print(y)

annotations = ["School", "A", "B", "C", "D"]

line1 = plt.plot([x], [y], "--ko", markersize = 5)

for a, label in enumerate(annotations):
    plt.annotate(label, (x[a], y[a]))


for x_cord, y_cord in zip(x, y):
    print(x_cord, y_cord)
        
axis = np.array([0, 4, 0 ,4])
plt.axis(axis)

l = line1.pop(0)
l.remove()

for i in range(1, num_of_stops + 2):
    traffic_cond = random.randint(1, 4)
    if traffic_cond == 1:
        plt.axhline(y = i - 1, xmin = i - 1, xmax = num_of_stops, c = "g", linewidth = 6.0)
    elif traffic_cond == 2:
        plt.axhline(y = i - 1, xmin = i - 1, xmax = num_of_stops, c = "y", linewidth = 6.0)
    elif traffic_cond == 3:
         plt.axhline(y = i - 1, xmin = i - 1, xmax = num_of_stops, c = "r", linewidth = 6.0)
   

plt.xticks(range(0, num_of_stops))
plt.yticks(range(0, num_of_stops))

plt.xlabel("Latitude")
plt.ylabel("Longitude")

plt.tight_layout()
plt.grid()
plt.show()

