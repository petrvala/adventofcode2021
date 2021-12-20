# Advent of Code 2021 day 07 part 1

from time import time


def read_input() -> list[int]:
    input_values = list()
    with open("./input_07.txt") as fn:
        input_line = fn.read()
    for input_value in input_line.split(","):
        input_values.append(int(input_value))
    return input_values


if __name__ == "__main__":

    timer_start = time()

    positions = read_input()
    print(f"Initial horizontal positions: {positions}")

    min_fuel = max(positions)**2
    min_fuel_position = 0
    for i in range(min(positions), max(positions)+1):
        this_level_fuel = 0
        for position in positions:
            this_level_fuel += abs(position - i)
        if this_level_fuel < min_fuel:
            min_fuel = this_level_fuel
            min_fuel_position = i

    print(f"Min fuel {min_fuel} spent at position {min_fuel_position}")

    timer_end = time()

    print(f"Computation takes {timer_end - timer_start} seconds.")
