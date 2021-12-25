# Advent of Code 2021 day 08 part 2

from time import time


def read_input() -> list[tuple[list[str], list[str]]]:
    input_values = list()
    with open("input_08.txt") as fn:
        input_lines = fn.read().splitlines()
    for input_line in input_lines:
        one_input = input_line.split(" | ")
        input_values.append((one_input[0].split(" "), one_input[1].split(" ")))
    return input_values


def evaluate_signal(signal_to_evaluate: str, evaluation_list: list[set[str]]) -> str:
    """Evaluate signal by going through computed evaluation list."""
    for position, one_eval in enumerate(evaluation_list):
        if one_eval == set(signal_to_evaluate):
            return str(position)
    raise RuntimeError(f"Cannot find correct evaluation for {signal_to_evaluate}")


if __name__ == "__main__":

    timer_start = time()

    input_digits = read_input()
    print(f"Input digits: {input_digits}")

    sum_signals = 0
    for digits in input_digits:
        dig_res = [set("") for _ in range(10)]
        for cluster in digits[0]:
            if len(cluster) == 2:
                dig_res[1] = set(cluster)
            elif len(cluster) == 3:
                dig_res[7] = set(cluster)
            elif len(cluster) == 4:
                dig_res[4] = set(cluster)
            elif len(cluster) == 7:
                dig_res[8] = set(cluster)
        for cluster in digits[0]:
            if len(cluster) == 5:
                if dig_res[1] <= set(cluster):
                    dig_res[3] = set(cluster)
                elif (dig_res[4] - dig_res[1]) <= set(cluster):
                    dig_res[5] = set(cluster)
                else:
                    dig_res[2] = set(cluster)
            if len(cluster) == 6:
                if dig_res[4] <= set(cluster):
                    dig_res[9] = set(cluster)
                elif dig_res[1] <= set(cluster):
                    dig_res[0] = set(cluster)
                else:
                    dig_res[6] = set(cluster)
        print(dig_res)
        str_eval = ""
        for cluster in digits[1]:
            str_eval += evaluate_signal(cluster, dig_res)
        print(f"Evaluation is {str_eval}")
        sum_signals += int(str_eval)

    print(f"Sum of signals is {sum_signals}")

    timer_end = time()

    print(f"Computation takes {timer_end - timer_start} seconds.")
