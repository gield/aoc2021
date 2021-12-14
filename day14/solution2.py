from collections import Counter


with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

polymer_template = lines[0]
insertion_rules = {pair: el for pair, el in (l.split(" -> ") for l in lines[2:])}

element_counter = Counter(polymer_template)
pair_counter = Counter(p1 + p2 for p1, p2 in zip(polymer_template, polymer_template[1:]))
for _ in range(40):
    for pair, num in pair_counter.copy().items():
        to_insert = insertion_rules[pair]
        pair_counter[pair] -= num
        pair_counter[pair[0] + to_insert] += num
        pair_counter[to_insert + pair[1]] += num
        element_counter[to_insert] += num

print(element_counter.most_common()[0][1] - element_counter.most_common()[-1][1])
