import itertools
from typing import List


def get_duplicate(backpacks) -> int:
    for i in itertools.chain(range(ord('a'), ord('z') + 1), range(ord('A'), ord('Z') + 1)):
        contained = True
        for backpack in backpacks:
            if chr(i) not in backpack:
                contained = False
                break
        if contained:
            return i


with open("rucksacks.txt", "r") as file:
    priority_sum: int = 0
    backpacks: List[str] = []
    for line in file:
        # Build up group
        line = line.strip()
        backpacks.append(line)
        if len(backpacks) != 3:
            continue

        # Process group
        duplicate = get_duplicate(backpacks)
        print(chr(duplicate))
        backpacks = []

        # Fetch priority
        priority: int
        if duplicate in range(ord("a"), ord("z") + 1):
            priority = duplicate - ord("a") + 1
        elif duplicate in range(ord("A"), ord("Z") + 1):
            priority = duplicate - ord("A") + 27

        priority_sum += priority

    print(priority_sum)
