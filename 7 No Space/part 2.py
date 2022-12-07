from typing import List
from Node import Node
from parse import parse

def main():
    lines: List[str] = open("stdinout.txt", "r").readlines()
    root: Node = parse(lines)

    total_space = 70000000
    current_used_space = len(root)
    free_space = total_space - current_used_space
    free_space_needed = 30000000
    space_to_be_freed = free_space_needed - free_space

    smallest_dir = root.find_smallest_dir_bigger_than(space_to_be_freed)
    print(smallest_dir)

if __name__ == '__main__':
    main()
