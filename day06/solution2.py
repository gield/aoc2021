with open("input.txt", "r") as f:
    line = f.readline().strip()

population = {i: 0 for i in range(9)}
for i in line.split(","):
    population[int(i)] += 1
for _ in range(256):
    num_new_fish = population[0]
    for i in range(8):
        population[i] = population[i + 1]
    population[6] += num_new_fish
    population[8] = num_new_fish
print(sum(population.values()))
