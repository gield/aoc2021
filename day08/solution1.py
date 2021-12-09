with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

appearances = 0
for line in lines:
    _, output_values = [s.split() for s in line.split(" | ")]
    appearances += sum(1 for d in output_values if len(d) in {2, 4, 3, 7})
print(appearances)
