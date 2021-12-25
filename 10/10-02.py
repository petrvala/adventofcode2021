# Advent of Code 2021 day 10 part 2

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


def evaluate_leftover_char(char: str) -> int:
    if char == "(":
        return 1
    elif char == "[":
        return 2
    elif char == "{":
        return 3
    elif char == "<":
        return 4
    else:
        raise ValueError(f"Leftover character '{char}' cannot be evaluated.")


if __name__ == "__main__":

    timer_start = time()

    check_lines = read_input()
    print(f"Input lines: {check_lines}")

    evaluations = list()
    for one_line in check_lines:
        stack = deque()
        for one_char in one_line:
            if check_closing(one_char):
                last_char = stack.pop()
                if not check_pair(last_char, one_char):
                    print(f"Illegal char '{one_char}', not evaluating")
                    break
            else:
                stack.append(one_char)
        else:
            left_chars_evaluation = 0
            while len(stack) > 0:
                left_chars_evaluation = left_chars_evaluation * 5 + evaluate_leftover_char(stack.pop())
            evaluations.append(left_chars_evaluation)

    print(f"Evaluation of incomplete chars is {evaluations}")
    print(f"Middle evaluation is {sorted(evaluations)[len(evaluations)//2]}")

    timer_end = time()

    print(f"Computation takes {timer_end - timer_start} seconds.")
