# Advent of Code 2021 day 09 part 1

from time import time


def read_input() -> list[list[int]]:
    input_values = list()
    with open("input_09.txt") as fn:
        input_lines = fn.read().splitlines()
    for input_line in input_lines:
        one_input = [int(x) for x in list(input_line)]
        input_values.append(one_input)
    return input_values


def check_lowest_point(row_pos: int, col_pos: int, map_to_check: list[list[int]]) -> bool:
    base_point = map_to_check[row_pos][col_pos]
    max_row = len(map_to_check) - 1
    max_col = len(map_to_check[0]) - 1
    if row_pos - 1 >= 0 and map_to_check[row_pos - 1][col_pos] <= base_point:
        return False
    if row_pos + 1 <= max_row and map_to_check[row_pos + 1][col_pos] <= base_point:
        return False
    if col_pos - 1 >= 0 and map_to_check[row_pos][col_pos - 1] <= base_point:
        return False
    if col_pos + 1 <= max_col and map_to_check[row_pos][col_pos + 1] <= base_point:
        return False
    return True


if __name__ == "__main__":

    timer_start = time()

    input_map = read_input()
    print(f"Input map: {input_map}")

    risk_levels = 0
    for row in range(len(input_map)):
        for col in range(len(input_map[0])):
            if check_lowest_point(row, col, input_map):
                print(f"Lowest point with value {input_map[row][col]} at {row}, {col}")
                risk_levels += 1 + input_map[row][col]

    print(f"Sum of risk levels is {risk_levels}")

    timer_end = time()

    print(f"Computation takes {timer_end - timer_start} seconds.")
