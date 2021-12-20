# Advent of Code 2021 day 06 part 2

from time import time
from collections import Counter


class CounterStates(object):

    max_state = 8

    def __init__(self, initial_states: list[int]):
        self.day = 0
        self.states = self.init_states(initial_states=initial_states)

    def init_states(self, initial_states: list[int]):
        states = [0 for _ in range(self.max_state + 1)]
        c = Counter(initial_states)
        for i in range(self.max_state + 1):
            states[i] = c.get(i, 0)
        return states

    def get_counter_states(self):
        return self.states

    def add_day(self) -> None:
        self.day += 1
        new_states = [0 for _ in range(self.max_state + 1)]
        for state, occurrence in enumerate(self.states):
            if state == 0:
                pass
            else:
                new_states[state-1] = occurrence
        new_states[8] = self.states[0]
        new_states[6] += self.states[0]
        self.states = new_states


def read_input() -> list[int]:
    input_values = list()
    with open("./input_06.txt") as fn:
        input_line = fn.read()
    for input_value in input_line.split(","):
        input_values.append(int(input_value))
    return input_values


if __name__ == "__main__":

    timer_start = time()

    days_in_aquarium = 256

    input_states = read_input()
    print(f"Initial state: {input_states}")

    counter = CounterStates(initial_states=input_states)
    for day in range(days_in_aquarium):
        counter.add_day()
    print(f"Fish counter after {days_in_aquarium} days: {sum(counter.states)}")

    timer_end = time()

    print(f"Computation takes {timer_end - timer_start} seconds.")
