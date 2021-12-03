with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

num_bits = len(lines[0])
ogr_lines = csr_lines = lines.copy()
for i in range(num_bits):
    most_common_bit = int(sum(int(l[i]) for l in ogr_lines) >= len(ogr_lines) / 2)
    ogr_lines = [l for l in ogr_lines if l[i] == str(most_common_bit)] or ogr_lines
    least_common_bit = int(sum(int(l[i]) for l in csr_lines) < len(csr_lines) / 2)
    csr_lines = [l for l in csr_lines if l[i] == str(least_common_bit)] or csr_lines
oxygen_generator_rating = int(ogr_lines[0], 2)
co2_scrubber_rating = int(csr_lines[0], 2)
print(oxygen_generator_rating * co2_scrubber_rating)
