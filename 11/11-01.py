# Advent of Code 2021 day 11 part 1

from time import time


def read_input() -> list[list[int]]:
    input_values = list()
    with open("input_11.txt") as fn:
        input_lines = fn.read().splitlines()
    for input_line in input_lines:
        one_input = [int(x) for x in list(input_line)]
        input_values.append(one_input)
    return input_values


class OctoMap(object):

    def __init__(self, entry_levels: list[list[int]]):
        self.octo_map = entry_levels
        self.step = 0
        self.max_row = len(self.octo_map)
        self.max_col = len(self.octo_map[0])
        self.flashes = 0

    def add_step(self):
        self.step += 1
        for row in range(self.max_row):
            for col in range(self.max_col):
                self.octo_map[row][col] += 1

    def make_flash(self):
        some_flash = True
        while some_flash:
            some_flash = False
            for row in range(self.max_row):
                for col in range(self.max_col):
                    if self.octo_map[row][col] > 9:
                        some_flash = True
                        self.octo_map[row][col] = 0
                        self._add_flash(row, col)

    def _add_flash(self, flash_row: int, flash_col):
        for offset in [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]:
            if 0 <= flash_row + offset[0] < self.max_row and 0 <= flash_col + offset[1] < self.max_col:
                if self.octo_map[flash_row + offset[0]][flash_col + offset[1]] != 0:
                    self.octo_map[flash_row + offset[0]][flash_col + offset[1]] += 1
                    if self.octo_map[flash_row + offset[0]][flash_col + offset[1]] > 9:
                        self.octo_map[flash_row + offset[0]][flash_col + offset[1]] = 0
                        self._add_flash(flash_row + offset[0], flash_col + offset[1])

    def count_flash(self):
        for row in range(self.max_row):
            for col in range(self.max_col):
                if self.octo_map[row][col] == 0:
                    self.flashes += 1

    def show_map(self):
        print(f"After step {self.step}:")
        for row in range(self.max_row):
            for col in range(self.max_col):
                print(self.octo_map[row][col], "\t", end="")
            print()


if __name__ == "__main__":

    timer_start = time()

    octo_input = read_input()
    print(f"Octopus map: {octo_input}")

    octo_map = OctoMap(entry_levels=octo_input)
    for step in range(1, 101):
        octo_map.add_step()
        octo_map.make_flash()
        octo_map.count_flash()
    octo_map.show_map()

    print(f"Sum of flashes is {octo_map.flashes}")

    timer_end = time()

    print(f"Computation takes {timer_end - timer_start} seconds.")
