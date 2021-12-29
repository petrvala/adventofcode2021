# Advent of Code 2021 day 09 part 2

from time import time
from collections import deque
from math import prod


def read_input() -> list[list[int]]:
    input_values = list()
    with open("input_09.txt") as fn:
        input_lines = fn.read().splitlines()
    for input_line in input_lines:
        one_input = [int(x) for x in list(input_line)]
        input_values.append(one_input)
    return input_values


class HeightMap(object):

    def __init__(self, height_map: list[list[int]]):
        self.height_map = height_map
        self.basins = list()
        self.already_visited = set()

    def check_for_basin(self):
        print(len(self.height_map), len(self.height_map[0]))

        for hrow in range(len(self.height_map)):
            for hcol in range(len(self.height_map[0])):
                print(hrow, hcol)
                if (hrow, hcol) in self.already_visited or self.height_map[hrow][hcol] == 9:
                    continue
                else:
                    this_basin = list()
                    stack = deque()
                    stack.append((hrow, hcol))
                    self.already_visited.add((hrow, hcol))

                while len(stack) > 0:
                    row, col = stack.pop()
                    this_basin.append((row, col))
                    if row - 1 >= 0 and self.height_map[row - 1][col] < 9 and \
                            (row - 1, col) not in self.already_visited:
                        stack.append((row - 1, col))
                        self.already_visited.add((row - 1, col))
                    if row + 1 < len(self.height_map) and self.height_map[row + 1][col] < 9 and \
                            (row + 1, col) not in self.already_visited:
                        stack.append((row + 1, col))
                        self.already_visited.add((row + 1, col))
                    if col - 1 >= 0 and self.height_map[row][col - 1] < 9 and \
                            (row, col - 1) not in self.already_visited:
                        stack.append((row, col - 1))
                        self.already_visited.add((row, col - 1))
                    if col + 1 < len(self.height_map[0]) and self.height_map[row][col + 1] < 9 and \
                            (row, col + 1) not in self.already_visited:
                        stack.append((row, col + 1))
                        self.already_visited.add((row, col + 1))

                self.basins.append(this_basin)

    def show_basins_length(self):
        print(f"I have {len(self.basins)} basins")
        for count, basin in enumerate(self.basins):
            print(f"Basin {count}: length {len(basin)} members {basin}")

    def show_multiplication_of_three_largest_basin(self):
        basins_area = list()
        for basin in self.basins:
            basins_area.append(len(basin))
        from_largest = sorted(basins_area, reverse=True)
        print(f"Three largest basins are of length {from_largest[:3]}")
        print(f"Their multiplication is {prod(from_largest[:3])}")


if __name__ == "__main__":

    timer_start = time()

    input_map = read_input()
    print(f"Input map: {input_map}")

    hmap = HeightMap(height_map=input_map)
    hmap.check_for_basin()
    hmap.show_basins_length()
    hmap.show_multiplication_of_three_largest_basin()

    timer_end = time()

    print(f"Computation takes {timer_end - timer_start} seconds.")
