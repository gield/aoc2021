with open("input.txt", "r") as f:
    line = f.readline().strip()

crabs = [int(i) for i in line.split(",")]
position_costs = [sum(abs(c - p) for c in crabs) for p in range(max(crabs) + 1)]
print(min(position_costs))
