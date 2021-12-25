# Advent of Code 2021 day 10 part 1

from time import time
from collections import deque


def read_input() -> list[str]:
    with open("input_10.txt") as fn:
        input_lines = fn.read().splitlines()
    return input_lines


def char_value(char: str) -> int:
    if char == ")":
        return 3
    elif char == "]":
        return 57
    elif char == "}":
        return 1197
    elif char == ">":
        return 25137
    else:
        raise ValueError(f"Character '{char}' cannot be evaluated.")


def check_pair(left: str, right: str) -> bool:
    if left == "(" and right == ")":
        return True
    if left == "[" and right == "]":
        return True
    if left == "{" and right == "}":
        return True
    if left == "<" and right == ">":
        return True
    return False


def check_closing(char: str) -> bool:
    if char in (")", "]", "}", ">"):
        return True
    return False


if __name__ == "__main__":

    timer_start = time()

    check_lines = read_input()
    print(f"Input lines: {check_lines}")

    char_values = 0
    for one_line in check_lines:
        stack = deque()
        for one_char in one_line:
            if check_closing(one_char):
                last_char = stack.pop()
                if not check_pair(last_char, one_char):
                    print(f"Illegal char '{one_char}': value {char_value(one_char)}")
                    char_values += char_value(one_char)
                    break
            else:
                stack.append(one_char)

    print(f"Sum of illegal chars values is {char_values}")

    timer_end = time()

    print(f"Computation takes {timer_end - timer_start} seconds.")
