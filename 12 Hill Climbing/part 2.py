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

    adjacency_list_reverse = {node: set([key for key, value in adjacency_list.items() if node in value]) for node in
                              adjacency_list}

    return adjacency_list_reverse


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


def BFS(adjacency_list, height_map, start_node, end_value):
    queue = [start_node, -1]
    visited = set()
    depth = 0
    while queue:
        node = queue.pop(0)
        if node == -1:
            depth += 1
            if len(queue) == 0:
                break
            queue.append(-1)
            continue

        if node not in visited:
            visited.add(node)
            if get_node_height(height_map, node) == end_value:
                return depth
            queue.extend(adjacency_list[node])
    return visited


def main():
    height_map = read_input("heightmap.txt")
    start_node, end_node = find_start_and_end(height_map)
    adjacency_list = build_adjacency_list(height_map)
    bfs_distance = BFS(adjacency_list, height_map, end_node, letter_map.index("a"))
    print(f"Part 2: {bfs_distance}")


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
