# Advent of Code 2021 day 06 part 1

from time import time


class LanternFish(object):

    cycle_length = 6

    def __init__(self, initial_timer: int):
        self.timer = initial_timer

    def add_cycle(self) -> bool:
        self.timer -= 1
        if self.timer < 0:
            self.timer = self.cycle_length
            return True
        return False


class Aquarium(object):

    new_fish_timer = LanternFish.cycle_length + 2

    def __init__(self, initial_fish_states: list[int]):
        self.day = 0
        self.aquarium = list()
        for ifs in initial_fish_states:
            self.aquarium.append(LanternFish(initial_timer=ifs))

    def add_day(self) -> None:
        self.day += 1
        newly_born_fish = list()
        for fish in self.aquarium:
            if fish.add_cycle():
                newly_born_fish.append(LanternFish(initial_timer=self.new_fish_timer))
        self.aquarium.extend(newly_born_fish)

    def show(self):
        fish_ages = list()
        for fish in self.aquarium:
            fish_ages.append(fish.timer)
        print(f"Day: {self.day} Fish: {fish_ages}")

    def count_fish(self):
        return len(self.aquarium)


def read_input() -> list[int]:
    input_values = list()
    with open("./input_06.txt") as fn:
        input_line = fn.read()
    for input_value in input_line.split(","):
        input_values.append(int(input_value))
    return input_values


if __name__ == "__main__":

    timer_start = time()

    days_in_aquarium = 140

    initial_state = read_input()
    print(f"Initial state: {initial_state}")

    my_aquarium = Aquarium(initial_fish_states=initial_state)
    for day in range(days_in_aquarium):
        my_aquarium.add_day()
    print(f"After {my_aquarium.day} days there is {my_aquarium.count_fish()} fish.")

    timer_end = time()

    print(f"Computation takes {timer_end - timer_start} seconds.")
