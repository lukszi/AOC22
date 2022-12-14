from typing import List, Mapping, Set, Tuple

letter_map = "SabcdefghijklmnopqrstuvwxyzE"

def read_input(filename: str) -> List[List[int]]:
    heightmap: List[List[int]] = []
    with open(filename, "r") as f:
        for line in f:
            heightmap.append([letter_map.index(height) for height in line.strip()])
    return heightmap


def build_adjacency_list(height_map: List[List[int]]) -> Mapping[int, Set[int]]:
    adjacency_list: Mapping[int, Set[int]] = {i: set() for i in range(len(height_map) * len(height_map[0]))}
    rows = len(height_map)
    columns = len(height_map[0])

    for node in range(rows * columns):
        current_height = get_node_height(height_map, node)
        for neighbour in get_neighbours(height_map, node):
            if get_node_height(height_map, neighbour) - current_height <= 1:
                adjacency_list[node].add(neighbour)
    return adjacency_list


def get_node_height(height_map: List[List[int]], node: int):
    row, column = get_node_address(height_map, node)
    return height_map[row][column]


def get_node_address(height_map, node) -> Tuple[int, int]:
    row_len = len(height_map[0])
    row = node // row_len
    column = node % row_len
    return row, column


def get_neighbours(height_map: List[List[int]], node: int):
    neigbour_offsets: List[Tuple[int, int]] = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    row, column = get_node_address(height_map, node)

    neighbours = [(row + offset[0]) * len(height_map[0]) + column + offset[1] for offset in neigbour_offsets]
    neighbours = [neighbour for neighbour in neighbours if is_in_map(height_map, neighbour)]

    return neighbours

def is_in_map(height_map, node):
    rows = len(height_map)
    columns = len(height_map[0])
    row = node // columns
    column = node % columns
    return 0 <= row < rows and 0 <= column < columns


def dijkstra(adjacency_list: Mapping[int, Set[int]], start: int, end: int) -> List[int]:
    # Initialize
    distances = {node: float("inf") for node in adjacency_list}
    distances[start] = 0
    predecessors = {node: None for node in adjacency_list}
    unvisited = set(adjacency_list)

    # Run algo
    while len(unvisited) != 0:
        current = min(unvisited, key=lambda node: distances[node])
        unvisited.remove(current)
        for neighbour in adjacency_list[current]:
            if neighbour in unvisited:
                new_distance = distances[current] + 1
                if new_distance < distances[neighbour]:
                    distances[neighbour] = new_distance
                    predecessors[neighbour] = current

    # Backtrace path
    path = []
    current = end
    while current != start:
        path.append(current)
        current = predecessors[current]
    path.append(start)
    path.reverse()
    return path

def draw_path(path: List[int], height: int, width: int):
    for i in range(height):
        for j in range(width):
            if i * width + j in path:
                # check if down up, left or right
                index = path.index(i * width + j)
                if index != len(path) - 1:
                    if path[index + 1] == i * width + j + 1:
                        print(">", end="")
                    elif path[index + 1] == i * width + j - 1:
                        print("<", end="")
                    elif path[index + 1] == (i + 1) * width + j:
                        print("v", end="")
                    elif path[index + 1] == (i - 1) * width + j:
                        print("^", end="")
                else:
                    print("E", end="")
            else:
                print(".", end="")
        print()


def main():
    height_map = read_input("heightmap.txt")
    start_node, end_node = find_start_and_end(height_map)
    adjacency_list = build_adjacency_list(height_map)
    path = dijkstra(adjacency_list, start_node, end_node)
    draw_path(path, len(height_map), len(height_map[0]))
    print(len(path)-1)


def find_start_and_end(height_map):
    end_node = 0
    start_node = 0
    for i, row in enumerate(height_map):
        for j, height in enumerate(row):
            if height == letter_map.index("E"):
                end_node = i * len(height_map[0]) + j
                height_map[i][j] = letter_map.index("z")
            if height == letter_map.index("S"):
                start_node = i * len(height_map[0]) + j
                height_map[i][j] = letter_map.index("a")

    return start_node, end_node


if __name__ == '__main__':
    main()