from collections import Counter


with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

polymer_template = lines[0]
insertion_rules = {pair: el for pair, el in (l.split(" -> ") for l in lines[2:])}

for _ in range(10):
    new_template = ""
    for p1, p2 in zip(polymer_template, polymer_template[1:]):
        new_template += p1 + insertion_rules[p1 + p2]
    polymer_template = new_template + polymer_template[-1]

element_counter = Counter(polymer_template)
print(element_counter.most_common()[0][1] - element_counter.most_common()[-1][1])
