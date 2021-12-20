# Advent of Code 2021 day 02 part 2

from dataclasses import dataclass


@dataclass
class Move:
    action: str
    points: int


with open("./input_02.txt") as fn:
    input_content = fn.read().splitlines()

print(input_content)
moves = [Move(m.split(' ')[0], int(m.split(' ')[1])) for m in input_content]
print(moves)

horizontal = 0
depth = 0
aim = 0

for move in moves:
    if move.action == "forward":
        horizontal = horizontal + move.points
        depth = depth + aim * move.points
    elif move.action == "down":
        aim = aim + move.points
    elif move.action == "up":
        aim = aim - move.points
    else:
        raise ValueError(f"Wrong action: {move.action}")

print("Horizontal:", horizontal)
print("Depth:", depth)
print("Multiplication:", horizontal * depth)
