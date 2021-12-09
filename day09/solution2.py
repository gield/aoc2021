import math

with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

height_map = {(r, c): int(lines[r][c]) for r in range(len(lines)) for c in range(len(lines[0]))}
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
low_points = []
for r in range(len(lines)):
    for c in range(len(lines[0])):
        for dr, dc in directions:
            if height_map[(r, c)] >= height_map.get((r + dr, c + dc), 9):
                break
        else:
            low_points.append((r, c))

basin_sizes = []
for low_point in low_points:
    basin = {low_point}
    to_check = {low_point}
    while to_check:
        r, c = to_check.pop()
        if height_map[(r, c)] == 9:
            continue
        basin.add((r, c))
        for dr, dc in directions:
            if (r + dr, c + dc) not in basin and (r + dr, c + dc) in height_map:
                to_check.add((r + dr, c + dc))
    basin_sizes.append(len(basin))
print(math.prod(sorted(basin_sizes)[-3:]))
