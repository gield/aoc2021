import itertools

with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

octopus_map = {(r, c): int(lines[r][c]) for r in range(len(lines)) for c in range(len(lines[0]))}
directions = [(r, c) for r in {-1, 0, 1} for c in {-1, 0, 1} if not (r == c == 0)]

for step in itertools.count():
    octopus_map = {(r, c): energy + 1 for (r, c), energy in octopus_map.items()}
    to_flash = {(r, c) for (r, c), energy in octopus_map.items() if energy > 9}
    has_flashed = set()
    while to_flash:
        r, c = to_flash.pop()
        has_flashed.add((r, c))
        for dr, dc in directions:
            if (r + dr, c + dc) not in octopus_map:
                continue
            octopus_map[(r + dr, c + dc)] += 1
            if (r + dr, c + dc) not in has_flashed and octopus_map[(r + dr, c + dc)] > 9:
                to_flash.add((r + dr, c + dc))
    for r, c in has_flashed:
        octopus_map[(r, c)] = 0
    if len(has_flashed) == 100:
        print(step + 1)
        break
