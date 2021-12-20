# Advent of Code 2021 day 03 part 1

from collections import Counter

with open("./input_03.txt") as fn:
    input_content = fn.read().splitlines()

print(input_content)

gama_rate = 0
epsilon_rate = 0

records = len(input_content)
print("Records:", records)

transposed = []
for i in range(len(input_content[0])):
    one_transposed = ""
    for j in range(records):
        one_transposed += input_content[j][i]
    transposed.append(one_transposed)

print(transposed)

frequency = [Counter(t).most_common(2) for t in transposed]
print("Frequency:", frequency)


def more_frequent(pair: list[tuple[str, int]]) -> str:
    if pair[0][1] < pair[1][1]:
        return pair[1][0]
    elif pair[0][1] > pair[1][1]:
        return pair[0][0]
    else:
        raise RuntimeError("Cannot get higher frequency for pair: %s", pair)


gamma = ""
for f in frequency:
    gamma += more_frequent(f)
print("Gamma binary:", gamma)

epsilon = ""
for char in gamma:
    if char == "0":
        epsilon += "1"
    else:
        epsilon += "0"
print("Epsilon binary", epsilon)

gama_rate = int(gamma, 2)
epsilon_rate = int(epsilon, 2)

print("Gamma rate:", gama_rate)
print("Epsilon rate:", epsilon_rate)
print("Consumption:", gama_rate * epsilon_rate)
