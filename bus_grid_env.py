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


count_x = Counter(x)
count_y = Counter(y)

result_x = [i for i, j in count_x.items() if j > 1]
result_y = [i for i, j in count_y.items() if j > 1]

for x_cord, y_cord in zip(x, y):
    plt.text(x_cord, y_cord + 0.15, '({}, {})'.format(x_cord, y_cord))
    if result_x != []:
        
    

print(count_x)
print(count_y)
print(result_x)
print(result_y)

axis = np.array([0, 4, 0 ,4])
plt.axis(axis)

l = line1.pop(0)
l.remove()

plt.xticks(range(0, num_of_stops))
plt.yticks(range(0, num_of_stops))

plt.xlabel("Latitude")
plt.ylabel("Longitude")

plt.tight_layout()
plt.grid()
#plt.show()