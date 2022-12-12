from typing import List


def read_file(file_name: str) -> List[List[int]]:
    with open(file_name, 'r') as file:
        return [[int(x) for x in line if x != "\n"] for line in file]


def count_visible_trees(height_map) -> int:
    visible_trees = len(height_map) * 2 + len(height_map[0]) * 2 - 4
    for i in range(1, len(height_map) - 1):
        for j in range(1, len(height_map[0]) - 1):
            visibility = [True] * 4
            for k in range(0, i):
                if height_map[k][j] >= height_map[i][j]:
                    visibility[0] = False
                    break
            if not visibility[0]:
                for k in range(i + 1, len(height_map)):
                    if height_map[k][j] >= height_map[i][j]:
                        visibility[1] = False
                        break
            if not visibility[0] and not visibility[1]:
                for k in range(0, j):
                    if height_map[i][k] >= height_map[i][j]:
                        visibility[2] = False
                        break
            if not visibility[0] and not visibility[1] and not visibility[2]:
                for k in range(j + 1, len(height_map[i])):
                    if height_map[i][k] >= height_map[i][j]:
                        visibility[3] = False
                        break
            if visibility[0] or visibility[1] or visibility[2] or visibility[3]:
                visible_trees += 1

    return visible_trees


def main ():
    height_map = read_file("map.txt")
    visibles = count_visible_trees(height_map)
    print(visibles)


if __name__ == '__main__':
    main()
