import numpy as np
from typing import List, Tuple

from numpy.core.records import ndarray


EMPTY = 0
WALL = 1
SAND = 2

drop_x = 500

def read_formations(file_name: str) -> List[List[tuple[int, int]]]:
    global drop_x
    with open(file_name, 'r') as file:
        formations = file.read().splitlines()

    formations = [[tuple([int(coord) for coord in point.split(",")]) for point in formation.split("->")] for formation in formations]

    return formations


def draw_formations(formations: List[List[tuple[int, int]]]) -> ndarray:
    x_max = max(max(x for x, y in formation) for formation in formations)
    y_max = max(max(y for x, y in formation) for formation in formations)
    sim = np.zeros((y_max + 1, x_max + 1), dtype=int)
    for formation in formations:
        for i in range(len(formation) - 1):
            x1, y1 = formation[i]
            x2, y2 = formation[i+1]
            if x1 == x2:
                # vertical line
                sim[min(y1, y2):max(y1, y2) + 1, x1] = WALL
            elif y1 == y2:
                sim[y1, min(x1,x2):max(x1,x2) + 1] = WALL

    return sim


def single_step(sim: ndarray, coord: tuple[int, int]) -> tuple[int, int]:
    if sim[coord[0] + 1, coord[1]] == EMPTY:
        sim[coord[0] + 1, coord[1]] = SAND
        sim[coord[0], coord[1]] = EMPTY
        return coord[0] + 1, coord[1]
    elif sim[coord[0] + 1, coord[1] - 1] == EMPTY:
        sim[coord[0] + 1, coord[1] - 1] = SAND
        sim[coord[0], coord[1]] = EMPTY
        return coord[0] + 1, coord[1] - 1
    elif sim[coord[0] + 1, coord[1] + 1] == EMPTY:
        sim[coord[0] + 1, coord[1] + 1] = SAND
        sim[coord[0], coord[1]] = EMPTY
        return coord[0] + 1, coord[1] + 1
    else:
        return coord


def simulate_sand_drop(sim: ndarray):
    # place sandcorn at drop_x
    coord = (0, drop_x)
    sim[coord] = SAND

    while True:
        new_coord = single_step(sim, coord)
        if new_coord == coord:
            break
        coord = new_coord

def main():
    formations = read_formations("rocks.txt")
    print(formations)
    sim = draw_formations(formations)
    counter = 0
    try:
        while True:
            simulate_sand_drop(sim)
            counter += 1
            print(sim)
    except IndexError:
        print(counter)


if __name__ == '__main__':
    main()