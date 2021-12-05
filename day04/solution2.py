import numpy as np
import sys

with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

drawn_numbers = [int(i) for i in lines[0].split(",")]
boards = np.array([[[
    int(i)
    for i in lines[b + r].split()]
    for r in range(5)]
    for b in range(2, len(lines), 6)])
masks = boards.copy()
masks.fill(0)

boards_won = [False] * len(boards)
for n in drawn_numbers:
    for j, (b, m) in enumerate(zip(boards, masks)):
        if boards_won[j] is True:
            continue
        m += np.asarray(b == n)
        for i in range(5):
            if np.sum(m[i]) == 5 or np.sum(m[:, i]) == 5:
                if sum(boards_won) != len(boards) - 1:
                    boards_won[j] = True
                    break
                else:
                    print(np.sum(np.sum((1 - m) * b)) * n)
                    sys.exit(0)
