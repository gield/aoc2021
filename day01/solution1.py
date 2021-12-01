with open("input.txt", "r") as f:
    numbers = [int(l.strip()) for l in f.readlines()]

print(sum(numbers[i + 1] > numbers[i] for i in range(len(numbers) - 1)))
