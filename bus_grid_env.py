import matplotlib.pyplot as plt
import numpy as np
import random
#Create 4 by 4 grid

num_of_stops = 4
x = []
y = []
for s in range(0, num_of_stops):
    o = random.uniform(0, num_of_stops)
    h = random.uniform(0, num_of_stops)
    if (o.is_integer() is False) and (h.is_integer() is False):
        if o > 2:
            o = random.randint(0, num_of_stops)
        elif o <= 2:
            h = random.randint(0, num_of_stops)
        
    x.append(o)
    y.append(h)
print(x)
print(y)
annotations = ["A", "B", "C", "D"]

line1 = plt.plot([x], [y], "ko")

for a, label in enumerate(annotations):
    plt.annotate(label, (x[a], y[a]))


plt.axis([0, 4, 0, 4])

l = line1.pop(0)
l.remove()

plt.xticks(range(0, num_of_stops + 1))
plt.yticks(range(0, num_of_stops + 1))

plt.xlabel("Latitude")
plt.ylabel("Longitude")

plt.tight_layout()
plt.grid()
plt.show()