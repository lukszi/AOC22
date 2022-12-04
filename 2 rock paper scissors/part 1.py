from typing import List, Mapping

diff_value_map: Mapping[int, int] = {0: 3, 1: 0, -2: 0, -1: 6, 2: 6}


def play_value(play: List[str]) -> int:
    elf_selection: int = ord(play[0]) - 65
    my_selection: int = ord(play[1]) - 88

    diff: int = elf_selection - my_selection
    value = diff_value_map[diff] + (my_selection + 1)

    return value


def main():
    value_sum: int = 0
    with open("strategy.txt", "r") as guide:
        for play in guide:
            value_sum += play_value(play.strip().split(" "))
    return value_sum


if __name__ == "__main__":
    print(main())
