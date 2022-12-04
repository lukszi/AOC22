from typing import Tuple


def process_line(line: str) -> Tuple[int, int]:
    split = line.strip().split(" ")
    instructions = (ord(split[0]) - 65, ord(split[1]) - 88)
    return instructions


def find_move(elf_move, outcome):
    # loose
    if outcome == 0:
        return (elf_move + 2) % 3
    # draw
    elif outcome == 1:
        return elf_move
    # win
    elif outcome == 2:
        return (elf_move + 1) % 3


def calc_value(my_move: int, outcome: int) -> int:
    move_val = my_move + 1
    outcome_val = outcome * 3
    return move_val + outcome_val


def main():
    value_sum: int = 0
    with open("strategy.txt", "r") as guide:
        for line in guide:
            (elf_move, outcome) = process_line(line)
            my_move = find_move(elf_move, outcome)
            value_sum += calc_value(my_move, outcome)

    return value_sum


if __name__ == "__main__":
    print(main())
