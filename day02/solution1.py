with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

horizontal = depth = 0
for line in lines:
    match line.split():
        case "forward", num:
            horizontal += int(num)
        case "down", num:
            depth += int(num)
        case "up", num:
            depth -= int(num)
print(horizontal * depth)
