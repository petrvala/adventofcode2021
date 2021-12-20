# Advent of Code 2021 day 04 part 1

import sys
from dataclasses import dataclass

import pandas as pd
from pandas import DataFrame as df


@dataclass
class MatrixCouple:
    numbers: df
    hits: df


def check_win(matrix: df) -> bool:
    print(f"Checking win for {matrix}")
    if matrix.all(axis=0).any():
        return True
    if matrix.all(axis=1).any():
        return True
    return False


def sum_not_drawn_numbers(matrices: MatrixCouple) -> int:
    sum_result = 0
    for mrow in range(matrices.hits.shape[0]):
        for mcol in range(matrices.hits.shape[1]):
            if matrices.hits._get_value(mrow, mcol) == False:
                sum_result += matrices.numbers._get_value(mrow, mcol)
    return sum_result


with open("./input_04.txt") as fn:
    input_lines = fn.read().splitlines()
    input_draws = input_lines[0].split(",")

    input_matrices = list()
    one_input_matrix = list()
    for input_line in input_lines[2:]:
        # print(input_line)
        if input_line == "":
            # print("adding matrix")
            input_matrices.append(one_input_matrix)
            one_input_matrix = []
        else:
            # print("adding one line")
            one_input_matrix.append(input_line.split(" "))
    # print("adding matrix")
    input_matrices.append(one_input_matrix)


input_draws = [int(input_draw) for input_draw in input_draws]
input_matrices = [[[int(input_matrix_number) for input_matrix_number in i if input_matrix_number != ""] for i in j] for j in input_matrices]
hit_matrix = pd.DataFrame(index=range(len(input_matrices[0])), columns=range(len(input_matrices[0][0])))
hit_matrix.fillna(False, inplace=True)

print(input_draws)
print(input_matrices)
print(hit_matrix)

df_matrices = []
for input_matrix in input_matrices:
    df_matrices.append(MatrixCouple(pd.DataFrame.from_records(input_matrix), hit_matrix.copy()))

for df_matrix in df_matrices:
    print(df_matrix)

for index, draw in enumerate(input_draws):
    print(f"Draw number {index} is {draw}.")
    for df_matrix in df_matrices:
        for row in range(df_matrix.numbers.shape[0]):
            for col in range(df_matrix.numbers.shape[1]):
                if df_matrix.numbers._get_value(row, col) == draw:
                    print(f"Hit at {row}, {col}")
                    df_matrix.hits.loc[row, col] = True
                    if check_win(df_matrix.hits):
                        print(f"There is a win in the draw number {index} - draw {draw}: {df_matrix}.")
                        not_drawn_sum = sum_not_drawn_numbers(df_matrix)
                        print(f"Sum of not drawn numbers: {not_drawn_sum}")
                        print(f"Final score: {not_drawn_sum * draw}")
                        sys.exit(0)
                    break

print("End of game matrices:")
for df_matrix in df_matrices:
    print(df_matrix)
