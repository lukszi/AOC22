from typing import List


def read_file(file_name: str) -> List[List[int]]:
    with open(file_name, 'r') as file:
        return [[int(x) for x in line if x != "\n"] for line in file]


def count_visible_trees(height_map) -> int:
    visible_trees = len(height_map) * 2 + len(height_map[0]) * 2 - 4
    for i in range(1, len(height_map) - 1):
        for j in range(1, len(height_map[0]) - 1):
            visible_left = True
            visible_right = True
            visible_top = True
            visible_bottom = True
            for k in range(0, i):
                if height_map[k][j] >= height_map[i][j]:
                    visible_top = False
                    break
            if not visible_top:
                for k in range(i + 1, len(height_map)):
                    if height_map[k][j] >= height_map[i][j]:
                        visible_bottom = False
                        break
            if not visible_top and not visible_bottom:
                for k in range(0, j):
                    if height_map[i][k] >= height_map[i][j]:
                        visible_left = False
                        break
            if not visible_top and not visible_bottom and not visible_left:
                for k in range(j + 1, len(height_map[i])):
                    if height_map[i][k] >= height_map[i][j]:
                        visible_right = False
                        break
            if visible_top or visible_bottom or visible_left or visible_right:
                visible_trees += 1

    return visible_trees


def main ():
    height_map = read_file("map.txt")
    visibles = count_visible_trees(height_map)
    print(visibles)


if __name__ == '__main__':
    main()
