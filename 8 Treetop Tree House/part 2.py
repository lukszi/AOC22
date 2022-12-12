from typing import List


def read_file(file_name: str) -> List[List[int]]:
    with open(file_name, 'r') as file:
        return [[int(x) for x in line if x != "\n"] for line in file]


def calc_max_scene(height_map) -> int:
    max_scene = 0
    for i in range(1, len(height_map) - 1):
        for j in range(1, len(height_map[0]) - 1):
            view_range = [0] * 4
            for k in reversed(range(0, i)):
                view_range[0] += 1
                if height_map[k][j] >= height_map[i][j]:
                    break
            for k in range(i + 1, len(height_map)):
                view_range[1] += 1
                if height_map[k][j] >= height_map[i][j]:
                    break
            for k in reversed(range(0, j)):
                view_range[2] += 1
                if height_map[i][k] >= height_map[i][j]:
                    break
            for k in range(j + 1, len(height_map[i])):
                view_range[3] += 1
                if height_map[i][k] >= height_map[i][j]:
                    break
            max_scene = max(max_scene, view_range[0] * view_range[1] * view_range[2] * view_range[3])
    return max_scene


def main ():
    height_map = read_file("map.txt")
    max_scene = calc_max_scene(height_map)
    print(max_scene)

if __name__ == '__main__':
    main()
