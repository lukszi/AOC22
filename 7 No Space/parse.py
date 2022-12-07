from typing import List

from Node import Node

def cd(work_dir: Node, line: str):
    name: str = line.split(" ")[2]
    if name == "..":
        parent = work_dir.parent
        work_dir = parent if parent is not None else work_dir
    elif name == "/":
        work_dir = work_dir.get_root()
    else:
        target_dir: Node | None = work_dir.find_named_child(name)
        if target_dir is None:
            raise "cd to non-existing folder"
        work_dir = target_dir
    return work_dir


def ls(work_dir: Node, lines: List[str]):

    for line in  lines:
        size, name = line.split(" ")
        if work_dir.find_named_child(name) is not None:
            break
        if size == "dir":
            work_dir.add_folder(name)
        else:
            work_dir.add_file(name, int(size))
    return work_dir

def parse(lines: List[str]) -> Node:
    work_dir: Node = Node("/", None)

    for i in range(len(lines)):
        line = lines[i].strip()
        if line.startswith("$ cd"):
            work_dir = cd(work_dir, line)
        elif line.startswith("$ ls"):
            relevant_lines = []
            for j in range(i+1, len(lines)):
                if lines[j].startswith("$"):
                    break
                relevant_lines.append(lines[j].strip())
            ls(work_dir, relevant_lines)
    return work_dir.get_root()
