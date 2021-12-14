with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

paper = {}
instructions = []
for l in lines:
    if l == "":
        continue
    elif "," in l:
        x, y = [int(i) for i in l.split(",")]
        paper[(x, y)] = "#"
    else:
        axis, num_str = l.split()[-1].split("=")
        num = int(num_str)
        instructions.append((axis, num))
max_x, max_y = [max(l) + 1 for l in zip(*paper.keys())]

for axis, num in instructions:
    if axis == "y":
        for i in range(max_y - num - 1):
            old_y = num + 1 + i
            new_y = num - 1 - i
            for x in range(max_x):
                if (x, old_y) in paper:
                    paper[(x, new_y)] = "#"
                    del paper[(x, old_y)]
        max_y = num
    else:
        for i in range(max_x - num - 1):
            old_x = num + 1 + i
            new_x = num - 1 - i
            for y in range(max_y):
                if (old_x, y) in paper:
                    paper[(new_x, y)] = "#"
                    del paper[(old_x, y)]
        max_x = num

for y in range(max_y):
    print("".join("#" if (x, y) in paper else " " for x in range(max_x)))
