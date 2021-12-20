# Advent of Code 2021 day 02 part 1

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

for move in moves:
    if move.action == "forward":
        horizontal = horizontal + move.points
    elif move.action == "down":
        depth = depth + move.points
    elif move.action == "up":
        depth = depth - move.points
    else:
        raise ValueError(f"Wrong action: {move.action}")

print("Horizontal:", horizontal)
print("Depth:", depth)
print("Multiplication:", horizontal * depth)
