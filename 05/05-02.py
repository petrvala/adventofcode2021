# Advent of Code 2021 day 05 part 2

from typing import Iterator

import pandas as pd


class Line(object):

    def __init__(self, x1: int, y1: int, x2: int, y2: int):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __repr__(self):
        return f"Line({self.x1},{self.y1} -> {self.x2},{self.y2})"

    def is_horizontal_vertical(self) -> bool:
        if self.x1 == self.x2 or self.y1 == self.y2:
            return True
        return False

    def verticals(self) -> tuple[int, int]:
        return self.y1, self.y2

    def horizontals(self) -> tuple[int, int]:
        return self.x1, self.x2

    def is_diagonal(self) -> bool:
        if abs(self.y2 - self.y1) == abs(self.x2 - self.x1):
            return True
        return False

    def is_drawable(self):
        if self.is_horizontal_vertical() or self.is_diagonal():
            return True
        return False


class Space(object):

    def __init__(self, rows: int, cols: int):
        self.space = pd.DataFrame(index=range(rows), columns=range(cols))
        self.space.fillna(0, inplace=True)

    def show(self):
        print(self.space)

    def draw_line(self, line_to_draw: Line) -> None:
        row_range = self.draw_range(line_to_draw.verticals())
        col_range = self.draw_range(line_to_draw.horizontals())
        for space_row in row_range:
            for space_col in col_range:
                self.space.loc[space_row, space_col] = self.space._get_value(space_row, space_col) + 1

    def draw_diagonal_line(self, line_to_draw: Line) -> None:
        draw_coordinates = self.diagonal_draw_coordinates(line_to_draw)
        for coordinate in draw_coordinates:
            space_row = coordinate[1]
            space_col = coordinate[0]
            self.space.loc[space_row, space_col] = self.space._get_value(space_row, space_col) + 1

    @staticmethod
    def diagonal_draw_coordinates(line_to_draw: Line) -> Iterator[tuple[int, int]]:
        iteration_range = abs(line_to_draw.x2 - line_to_draw.x1)
        for i in range(iteration_range + 1):
            if line_to_draw.x1 < line_to_draw.x2:
                x_to_draw = line_to_draw.x1 + i
            else:
                x_to_draw = line_to_draw.x1 - i
            if line_to_draw.y1 < line_to_draw.y2:
                y_to_draw = line_to_draw.y1 + i
            else:
                y_to_draw = line_to_draw.y1 - i
            yield x_to_draw, y_to_draw

    @staticmethod
    def draw_range(coordinates_for_range: tuple[int, int]) -> range:
        if coordinates_for_range[0] < coordinates_for_range[1]:
            return range(coordinates_for_range[0], coordinates_for_range[1]+1)
        return range(coordinates_for_range[1], coordinates_for_range[0]+1)

    def number_of_overlaps(self) -> int:
        overlaps = 0
        for space_row in range(self.space.shape[0]):
            for space_col in range(self.space.shape[1]):
                if self.space._get_value(space_row, space_col) >= 2:
                    overlaps += 1
        return overlaps


def read_input() -> list[Line]:
    parsed_input_lines = list()
    with open("./input_05.txt") as fn:
        input_lines = fn.read().splitlines()
        for input_line in input_lines:
            splitted_input_line = input_line.split(" -> ")
            splitted_first = splitted_input_line[0].split(",")
            splitted_second = splitted_input_line[1].split(",")
            parsed_input_lines.append(Line(int(splitted_first[0]), int(splitted_first[1]),
                                           int(splitted_second[0]), int(splitted_second[1])))
    return parsed_input_lines


def get_max_coordinates(input_lines: list[Line]) -> tuple[int, int]:
    max_row = 0
    max_col = 0
    for input_line in input_lines:
        if input_line.x1 > max_col:
            max_col = input_line.x1
        if input_line.x2 > max_col:
            max_col = input_line.x2
        if input_line.y1 > max_row:
            max_row = input_line.y1
        if input_line.y2 > max_row:
            max_row = input_line.y2
    return max_row + 1, max_col + 1


if __name__ == "__main__":

    lines = read_input()
    max_coordinates = get_max_coordinates(lines)
    print(f"Space range is {max_coordinates}")

    for line in lines:
        if line.is_horizontal_vertical():
            print(f"Horizontal or vertical input line: {line}")
        if line.is_diagonal():
            print(f"Diagonal input line: {line}")
            # print(list(Space(0, 0).diagonal_draw_coordinates(line)))

    my_space = Space(*max_coordinates)
    print("My space:")
    for line in lines:
        if line.is_horizontal_vertical():
            my_space.draw_line(line)
        if line.is_diagonal():
            my_space.draw_diagonal_line(line)
    my_space.show()
    print(f"Overlaps: {my_space.number_of_overlaps()}")
