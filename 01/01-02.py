# Advent of Code 2021 day 01 part 2

with open("./input_01.txt") as fn:
    input_content = fn.read().splitlines()

print(input_content)

sliding_sums = list()
for i in range(0, len(input_content)):
    if i + 2 < len(input_content):
        sliding_sums.append(sum([int(input_content[i]), int(input_content[i+1]), int(input_content[i+2])]))

print(sliding_sums)

counter = 0
for i in range(1, len(sliding_sums)):
    if sliding_sums[i-1] < sliding_sums[i]:
        counter += 1

print("Increases:", counter)
