with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

horizontal, depth, aim = 0, 0, 0
for line in lines:
    instruction, num = line.split()
    if instruction == "forward":
        horizontal += int(num)
        depth += aim * int(num)
    elif instruction == "down":
        aim += int(num)
    elif instruction == "up":
        aim -= int(num)
print(horizontal * depth)
