with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

horizontal = depth = aim = 0
for line in lines:
    match line.split():
        case "forward", num:
            horizontal += int(num)
            depth += aim * int(num)
        case "down", num:
            aim += int(num)
        case "up", num:
            aim -= int(num)
print(horizontal * depth)
