from queue import PriorityQueue


with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

cave = {}
num_y, num_x = len(lines), len(lines[0])
for y in range(num_y):
    for x in range(num_x):
        cave[(x, y)] = int(lines[y][x])

costs = {(0, 0): 0}
visited = set()
to_visit = PriorityQueue()
to_visit.put((0, (0, 0)))
while not to_visit.empty():
    cost, node = to_visit.get()
    visited.add(node)
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        neighbor = node[0] + dx, node[1] + dy
        if neighbor in cave and neighbor not in visited:
            old_cost = costs.get(neighbor, float("inf"))
            new_cost = costs[node] + cave[neighbor]
            if new_cost < old_cost:
                to_visit.put((new_cost, neighbor))
                costs[neighbor] = new_cost

print(costs[(num_x - 1, num_y - 1)])
