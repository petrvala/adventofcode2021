# Advent of Code 2021 day 03 part 2

from collections import Counter


def transpose(list_records: list[str]) -> list[str]:
    transposed_list = []
    for i in range(len(list_records[0])):
        one_transposed = ""
        for j in range(len(list_records)):
            one_transposed += list_records[j][i]
        transposed_list.append(one_transposed)
    return transposed_list


def more_frequent(pair: list[tuple[str, int]], prevails: str = "X") -> str:
    if pair[0][1] < pair[1][1]:
        return pair[1][0]
    elif pair[0][1] > pair[1][1]:
        return pair[0][0]
    else:
        return prevails


def less_frequent(pair: list[tuple[str, int]], prevails: str = "X") -> str:
    if pair[0][1] < pair[1][1]:
        return pair[0][0]
    elif pair[0][1] > pair[1][1]:
        return pair[1][0]
    else:
        return prevails


def negate(char_number: str) -> str:
    if char_number == "1":
        return "0"
    elif char_number == "0":
        return "1"
    else:
        raise ValueError(f"Cannot negate this character number: {char_number}")


def filter_inputs_by_bit(inputs: list[str], position_in_input: int, bit_value: str) -> list[str]:
    return [inp for inp in inputs if inp[position_in_input] == bit_value]


with open("./input_03.txt") as fn:
    input_content = fn.read().splitlines()

print(input_content)

records = len(input_content)
print("Records:", records)

directions_result = dict()
for direction in ("1", "0"):
    left_inputs = input_content.copy()
    for pos in range(len(input_content[0])):

        print(f"Direction-Position: {direction}-{pos}")

        transposed = transpose(left_inputs)
        print("Transposed:", transposed)

        frequency = Counter(transposed[pos]).most_common(2)
        print("Frequency:", frequency)

        if direction == "1":
            win_direction = more_frequent(pair=frequency, prevails="1")
        else:
            win_direction = less_frequent(pair=frequency, prevails="0")
        left_inputs = filter_inputs_by_bit(inputs=left_inputs, position_in_input=pos, bit_value=win_direction)
        print("Left inputs:", left_inputs)
        if len(left_inputs) <= 1:
            directions_result[direction] = left_inputs
            break


oxygen_generation_rating = directions_result["1"][0]
print("oxygen generation rating binary:", oxygen_generation_rating)

co2_scrubber_rating = directions_result["0"][0]
print("CO2 scrubber rating binary", co2_scrubber_rating)

oxygen_generation_rating = int(oxygen_generation_rating, 2)
co2_scrubber_rating = int(co2_scrubber_rating, 2)

print("oxygen generation rating:", oxygen_generation_rating)
print("CO2 scrubber rating:", co2_scrubber_rating)
print("life support rating:", oxygen_generation_rating * co2_scrubber_rating)
