# Advent of Code 2021 day 12 part 1

from time import time


def read_input() -> list[str]:
    with open("input_12.txt") as fn:
        input_lines = fn.read().splitlines()
    return input_lines


class Passage(object):

    def __init__(self, possible_ways: list[str]):
        self.ways = self.create_all_possible_ways(possible_ways)
        self.finishing_ways = []

    @staticmethod
    def create_all_possible_ways(possible_ways: list[str]) -> list[tuple[str, str]]:
        all_possible_ways = []
        for way in possible_ways:
            split_way = way.split("-")
            all_possible_ways.append((split_way[0], split_way[1]))
            if split_way[0] != "start" and split_way[1] != "end":
                all_possible_ways.append((split_way[1], split_way[0]))
        return all_possible_ways

    def make_move(self, move_from: str, already_moved: list[str]):
        for move in self.ways:
            print(f"Evaluating move '{move}'")
            if move_from in move[0]:
                if move[1].islower() and move[1] in already_moved:
                    print(f"Cannot move to '{move[1]}'")
                elif move[1] == "end":
                    already_moved.append(move[1])
                    print(already_moved)
                    self.finishing_ways.append(already_moved.copy())
                    already_moved.pop()
                else:
                    print(f"Making move to '{move[1]}'")
                    already_moved.append(move[1])
                    self.make_move(move[1], already_moved=already_moved)
                    already_moved.pop()

    def show_all_ways(self):
        print(self.ways)


if __name__ == "__main__":

    timer_start = time()

    input_paths = read_input()
    print(f"Input paths: {input_paths}")

    passage = Passage(input_paths)
    passage.show_all_ways()
    passage.make_move("start", ["start"])
    print(f"All possible ways: {passage.finishing_ways}")
    print(f"All possible ways count: {len(passage.finishing_ways)}")

    timer_end = time()

    print(f"Computation takes {timer_end - timer_start} seconds.")
