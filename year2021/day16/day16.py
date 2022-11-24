# I completely rewrote the entire script after part 1...

from functools import reduce

table = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}

def solve(string):
    if all(x == '0' for x in string):
        return (len(string), 0, 0)
    packet_version = int(string[0:3], 2)
    packet_id = int(string[3:6], 2)
    length = 6
    packets = 1
    total_version = packet_version
    value = 0
    if packet_id == 4:
        last_group = False
        groups = []
        while not last_group:
            last_group = string[length] == '0'
            group = string[length + 1 : length + 5]
            groups.append(group)
            length += 5
        value = int(''.join(groups), 2)
    else:
        length_type = string[length]
        values = []
        if length_type == '0':
            # next 15 bits represent total length in bits of sub-packets
            number_of_bits = int(string[length + 1 : length + 16], 2)
            length += 16
            bits_solved = 0
            while bits_solved < number_of_bits:
                next_string = string[length + bits_solved : length + number_of_bits]
                next_length, next_packets, next_version, next_value = solve(next_string)
                bits_solved += next_length
                total_version += next_version
                values.append(next_value)
            length += number_of_bits
        else:
            # next 11 bits represent number of sub-packets immediately contained
            number_of_packets = int(string[length + 1 : length + 12], 2)
            length += 12
            packets_solved = 0
            while packets_solved < number_of_packets:
                next_string = string[length :]
                next_length, next_packets, next_version, next_value = solve(next_string)
                length += next_length
                packets_solved += next_packets
                total_version += next_version
                values.append(next_value)
        if packet_id == 0:
            value = sum(values)
        elif packet_id == 1:
            value = reduce(lambda x, y: x * y, values)
        elif packet_id == 2:
            value = reduce(lambda x, y: min(x, y), values)
        elif packet_id == 3:
            value = reduce(lambda x, y: max(x, y), values)
        elif packet_id == 5:
            value = 1 if values[0] > values[1] else 0
        elif packet_id == 6:
            value = 1 if values[0] < values[1] else 0
        elif packet_id == 7:
            value = 1 if values[0] == values[1] else 0
    return (length, packets, total_version, value)

# data = "A0016C880162017C3686B18A3D4780" # for testing
with open("AoC 2021/day16/a.in") as f:
    data = f.read()
bits = "".join(table[x] for x in data)
length, packets, total_version, value = solve(bits)
print("Part 1:", total_version)
print("Part 2:", value)
