from typing import List, Tuple

head_pos = [0, 0]
tail_pos = [0, 0]

visited_positions = set()
visited_positions.add(tuple(tail_pos))
draw = False



def draw_current_state(print_visited=False):
    for y in range(0, 5):
        for x in range(0, 6):
            if (x, y) == tuple(head_pos):
                print("H", end="")
            elif (x, y) == tuple(tail_pos):
                print("T", end="")
            elif (x, y) in visited_positions and print_visited:
                print("#", end="")
            else:
                print(".", end="")
        print()
    print()

def sign(x):
    return x//abs(x)

def simulate_single_step(direction):
    global head_pos, tail_pos
    # Move head
    if direction == "U":
        head_pos[1] += 1
    elif direction == "D":
        head_pos[1] -= 1
    elif direction == "L":
        head_pos[0] -= 1
    elif direction == "R":
        head_pos[0] += 1

    # Adjust tail
    dist = [head_pos[0] - tail_pos[0], head_pos[1] - tail_pos[1]]
    if abs(dist[0]) <= 1 and abs(dist[1]) <= 1:
        return
    if abs(dist[0]) > 2 and abs(dist[1]) > 2:
        raise Exception("Tail too far removed")
    # Tail not adjacent, move it
    else:
        if abs(dist[0]) == 0 and abs(dist[1]) == 2:
            tail_pos[1] += 1 * sign(dist[1])
        elif abs(dist[0]) == 2 and abs(dist[1]) == 0:
            tail_pos[0] += 1 * sign(dist[0])
        elif abs(dist[0]) == 2 and abs(dist[1]) == 1:
            tail_pos[0] += 1 * sign(dist[0])
            tail_pos[1] += 1 * sign(dist[1])
        elif abs(dist[0]) == 1 and abs(dist[1]) == 2:
            tail_pos[0] += 1 * sign(dist[0])
            tail_pos[1] += 1 * sign(dist[1])

    visited_positions.add(tuple(tail_pos))



def simulate_motion(direction: str, distance: int):
    if draw:
        print(f"== {direction} {distance} ==")
    for _ in range(distance):
        simulate_single_step(direction)
        if abs(head_pos[0] - tail_pos[0]) > 1 or abs(head_pos[1] - tail_pos[1]) > 1:
            raise Exception("Tail not adjacent to head")
        if draw:
            draw_current_state()

def main():
    motions = read_input("motions.txt")
    if draw:
        print("== Initial State ==")
        draw_current_state()
    for direction, distance in motions:
        simulate_motion(direction, distance)

    print(len(visited_positions))



def read_input(file_name: str) -> List[Tuple[str, int]]:
    with open(file_name) as f:
        lines = f.read().split("\n")
        return [(line[0], int(line[2:])) for line in lines]


if __name__ == "__main__":
    main()
