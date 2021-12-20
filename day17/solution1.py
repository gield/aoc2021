with open("input.txt", "r") as f:
    line = f.read().strip()

x_range, y_range = [range(int(i), int(j) + 1)
                    for i, j in [raw_range[2:].split("..")
                    for raw_range in line[13:].split(", ")]]


def get_max_height(vx: int, vy: int) -> int:
    x = y = highest_y = 0
    while True:
        x += vx
        y += vy
        if y > highest_y:
            highest_y = y
        if x in x_range and y in y_range:
            return highest_y
        if x > x_range[-1] or y < y_range[0]:
            return 0  # miss
        if vx > 0:
            vx -= 1
        if vx < 0:
            vx += 1
        vy -= 1


max_y = max(abs(i) for i in y_range)
print(max(get_max_height(vx, vy)
          for vy in range(-max_y, max_y)
          for vx in range(x_range[-1] + 1)))
