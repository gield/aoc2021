with open("input.txt", "r") as f:
    numbers = [int(l.strip()) for l in f.readlines()]

print(sum(sum(numbers[i + 1:i + 4]) > sum(numbers[i:i + 3]) for i in range(len(numbers) - 3)))
