# Advent of Code 2021 day 08 part 1

from time import time


def read_input() -> list[tuple[list[str], list[str]]]:
    input_values = list()
    with open("input_08.txt") as fn:
        input_lines = fn.read().splitlines()
    for input_line in input_lines:
        one_input = input_line.split(" | ")
        input_values.append((one_input[0].split(" "), one_input[1].split(" ")))
    return input_values


if __name__ == "__main__":

    timer_start = time()

    input_digits = read_input()
    print(f"Input digits: {input_digits}")

    signals = 0
    for digits in input_digits:
        for cluster in digits[1]:
            if len(cluster) in [2, 3, 4, 7]:
                signals += 1

    print(f"Number of signals is {signals}")

    timer_end = time()

    print(f"Computation takes {timer_end - timer_start} seconds.")
