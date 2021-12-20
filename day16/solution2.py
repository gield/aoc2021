import math
from typing import Tuple


def parse(packet: str) -> Tuple[int, str]:
    type_id = int(packet[3:6], 2)
    if type_id == 4:  # literal value
        number, rest = parse_literal_value(packet[6:])
        return number, rest
    else:  # operator
        length_type_id = packet[6]
        if length_type_id == "0":
            len_packets = int(packet[7:22], 2)
            rest = packet[22:22 + len_packets]
            numbers = []
            while rest:
                num, rest = parse(rest)
                numbers.append(num)
            rest = packet[22 + len_packets:]
        else:
            num_packets = int(packet[8:18], 2)
            rest = packet[18:]
            numbers = []
            for _ in range(num_packets):
                num, rest = parse(rest)
                numbers.append(num)
        match type_id:
            case 0: return sum(numbers), rest
            case 1: return math.prod(numbers), rest
            case 2: return min(numbers), rest
            case 3: return max(numbers), rest
            case 5: return int(numbers[0] > numbers[1]), rest
            case 6: return int(numbers[0] < numbers[1]), rest
            case 7: return int(numbers[0] == numbers[1]), rest


def parse_literal_value(sub_packet: str) -> Tuple[int, str]:
    literal_value = ""
    for i in range(0, len(sub_packet), 5):
        literal_value += sub_packet[i + 1:i + 5]
        if sub_packet[i] == "0":
            break
    return int(literal_value, 2), sub_packet[i + 5:]


with open("input.txt", "r") as f:
    line = f.read().strip()

binary = bin(int(line, 16))[2:].zfill(len(line) * 4)
result, _ = parse(binary)
print(result)
