with open("input.txt", "r") as f:
    line = f.readline().strip()


def cost(crab: int, proposed_position: int) -> int:
    distance = abs(crab - proposed_position)
    return int(distance * (distance + 1) / 2)


crabs = [int(i) for i in line.split(",")]
position_costs = [sum(cost(c, p) for c in crabs) for p in range(max(crabs) + 1)]
print(min(position_costs))
