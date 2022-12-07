from typing import List
from parse import parse

def main():
    lines: List[str] = open("stdinout.txt", "r").readlines()
    root = parse(lines)
    smaller_dirs = root.get_all_dirs_smaller_than(100000)
    print(sum(list(map(len, smaller_dirs))))

if __name__ == '__main__':
    main()
