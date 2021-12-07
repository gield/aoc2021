import numpy as np

with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

floor = np.zeros((1000, 1000), dtype=int)
for line in lines:
    x1, y1, x2, y2 = [int(i) for i in line.replace(" -> ", ",").split(",")]
    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            floor[x1, y] += 1
    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            floor[x, y1] += 1
    else:
        for i in range(max(y1, y2) - min(y1, y2) + 1):
            x = x1 + i if x1 < x2 else x1 - i
            y = y1 + i if y1 < y2 else y1 - i
            floor[x, y] += 1

print(np.sum(np.sum(floor > 1)))
