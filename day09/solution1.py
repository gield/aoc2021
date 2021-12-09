with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

height_map = {(r, c): int(lines[r][c]) for r in range(len(lines)) for c in range(len(lines[0]))}
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
low_points_sum = 0
for r in range(len(lines)):
    for c in range(len(lines[0])):
        for dr, dc in directions:
            if height_map[(r, c)] >= height_map.get((r + dr, c + dc), 9):
                break
        else:
            low_points_sum += height_map[(r, c)] + 1
print(low_points_sum)
