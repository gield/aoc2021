with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

num_bits = len(lines[0])
common_bits = ""
for i in range(num_bits):
    bit = int(sum(int(l[i]) for l in lines) > len(lines) / 2)
    common_bits += str(bit)
gamma_rate = int(common_bits, 2)
epsilon_rate = gamma_rate ^ int("1" * num_bits, 2)
power_consumption = gamma_rate * epsilon_rate
print(power_consumption)
