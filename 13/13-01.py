# Advent of Code 2021 day 13 part 1

from time import time
from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


@dataclass
class Fold:
    axis: str
    where: int


def read_input() -> tuple[list[Point], list[Fold]]:
    with open("input_13.txt") as fn:
        input_lines = fn.read().splitlines()
    input_flag = False
    input_points = list()
    input_folds = list()
    for input_line in input_lines:
        if input_line == "":
            input_flag = True
            continue
        if not input_flag:
            point_parts = input_line.split(",")
            input_points.append(Point(x=int(point_parts[0]), y=int(point_parts[1])))
        else:
            fold_parts = input_line.split("=")
            input_folds.append(Fold(axis=fold_parts[0][-1:], where=int(fold_parts[1])))

    return input_points, input_folds


class Board(object):
    def __init__(self):
        self.board = None

    def initialize_board(self, base_points: list[Point]):
        max_x = 0
        max_y = 0
        for point in base_points:
            if point.x > max_x:
                max_x = point.x
            if point.y > max_y:
                max_y = point.y
        self.board = [[False for _ in range(max_x + 1)] for _ in range(max_y + 1)]

        for point in base_points:
            self.board[point.y][point.x] = True

    def make_fold(self, fold: Fold):
        print(f"Making fold {fold}:")
        max_x = len(self.board[0])
        max_y = len(self.board)
        if fold.axis == "x":
            new_board = [[False for _ in range(fold.where)] for _ in range(max_y)]

            for row in range(max_y):
                for col in range(fold.where):
                    new_board[row][col] = self.board[row][col]
                for col in range(fold.where + 1, max_x):
                    if self.board[row][col]:
                        new_board[row][max_x - col - 1] = self.board[row][col]

        elif fold.axis == "y":
            new_board = [[False for _ in range(max_x)] for _ in range(fold.where)]

            for row in range(fold.where):
                for col in range(max_x):
                    new_board[row][col] = self.board[row][col]
            for row in range(fold.where + 1, max_y):
                for col in range(max_x):
                    if self.board[row][col]:
                        new_board[max_y - row - 1][col] = self.board[row][col]

        else:
            raise ValueError(f"Unknown axis {fold.axis} to fold.")

        self.board = new_board

    def show_board(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if self.board[row][col]:
                    print("#", end="")
                else:
                    print(".", end="")
            print()

    def count_board(self):
        counter = 0
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if self.board[row][col]:
                    counter += 1
        return counter


if __name__ == "__main__":

    timer_start = time()

    input_data = read_input()
    print(f"Input data: {input_data}")
    points = input_data[0]
    folds = input_data[1]

    board = Board()
    board.initialize_board(base_points=points)
    board.make_fold(fold=folds[0])
    board.show_board()

    print(f"Visible dots in board: {board.count_board()}")

    timer_end = time()

    print(f"Computation takes {timer_end - timer_start} seconds.")
