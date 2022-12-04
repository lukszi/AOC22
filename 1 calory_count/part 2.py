from typing import List
from bisect import insort

top_3: List[int] = [0, 0, 0]
current_count: int = 0


def insert(l: List[int], item: int):
    l.pop()
    insort(l, item, key=lambda x: -x)


with open("calories.txt", "r") as file:
    for line in file:
        if line == "\n":
            if min(top_3) < current_count:
                insert(top_3, current_count)
            current_count = 0
        else:
            current_count += (int(line))

print(top_3)
