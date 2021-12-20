# Advent of Code 2021 day 01 part 1

with open("./input_01.txt") as fn:
    input_content = fn.read().splitlines()

print(input_content)

counter = 0
for i in range(1, len(input_content)):
    if int(input_content[i-1]) < int(input_content[i]):
        counter += 1

print("Increases:", counter)
