with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

horizontal, depth = 0, 0
for line in lines:
    instruction, num = line.split()
    if instruction == "forward":
        horizontal += int(num)
    elif instruction == "down":
        depth += int(num)
    elif instruction == "up":
        depth -= int(num)
print(horizontal * depth)
