from typing import Tuple


def parse(packet: str) -> Tuple[int, str]:
    global sum_versions

    packet_version = int(packet[:3], 2)
    sum_versions += packet_version
    type_id = int(packet[3:6], 2)
    if type_id == 4:  # literal value
        number, rest = parse_literal_value(packet[6:])
        return number, rest
    else:  # operator
        length_type_id = packet[6]
        if length_type_id == "0":
            len_packets = int(packet[7:22], 2)
            rest = packet[22:22 + len_packets]
            while rest:
                _, rest = parse(rest)
            rest = packet[22 + len_packets:]
            return 0, rest
        else:
            num_packets = int(packet[8:18], 2)
            rest = packet[18:]
            for _ in range(num_packets):
                _, rest = parse(rest)
            return 0, rest


def parse_literal_value(sub_packet: str) -> Tuple[int, str]:
    literal_value = ""
    for i in range(0, len(sub_packet), 5):
        literal_value += sub_packet[i + 1:i + 5]
        if sub_packet[i] == "0":
            break
    return int(literal_value, 2), sub_packet[i + 5:]


with open("input.txt", "r") as f:
    line = f.read().strip()

sum_versions = 0
binary = bin(int(line, 16))[2:].zfill(len(line) * 4)
parse(binary)
print(sum_versions)
