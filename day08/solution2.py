with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

total_sum = 0
for line in lines:
    signal_wires, output_values = [s.split() for s in line.split(" | ")]
    signal_1 = [set(s) for s in signal_wires if len(s) == 2][0]
    signal_4 = [set(s) for s in signal_wires if len(s) == 4][0]
    signal_7 = [set(s) for s in signal_wires if len(s) == 3][0]
    signals_069 = [set(s) for s in signal_wires if len(s) == 6]

    top = signal_7 - signal_1
    common_069 = signals_069[0] & signals_069[1] & signals_069[2] - top
    top_left = (signal_4 - signal_1) & common_069
    bottom_right = signal_1 & common_069
    top_right = signal_1 - bottom_right
    middle = signal_4 - signal_1 - top_left
    leftover_069 = [s - top - top_left - bottom_right - top_right - middle for s in signals_069]
    bottom = [set(s) for s in leftover_069 if len(s) == 1][0]
    bottom_left = [set(s) for s in leftover_069 if len(s) == 2][0] - bottom

    mapping = {
        "".join(sorted(top | top_left | top_right | bottom_left | bottom_right | bottom)): 0,
        "".join(sorted(signal_1)): 1,
        "".join(sorted(top | top_right | middle | bottom_left | bottom)): 2,
        "".join(sorted(top | top_right | middle | bottom_right | bottom)): 3,
        "".join(sorted(signal_4)): 4,
        "".join(sorted(top | top_left | middle | bottom_right | bottom)): 5,
        "".join(sorted(top | top_left | middle | bottom_left | bottom_right | bottom)): 6,
        "".join(sorted(signal_7)): 7,
        "abcdefg": 8,
        "".join(sorted(top | top_left | top_right | middle | bottom_right | bottom)): 9,
    }
    digits = [str(mapping["".join(sorted(v))]) for v in output_values]
    total_sum += int("".join(digits))
print(total_sum)
