from __future__ import annotations

from typing import List


class Node:
    children: List[Node]
    size: int = None
    parent: Node | None = None
    name: str = None
    def __init__(self, name, parent: Node | None, size: int | None = None):
        self.children = []
        self.left = None
        self.right = None
        self.size = size
        self.name = name
        self.parent = parent

    def add_folder(self, name: str):
        new_folder = Node(name, self)
        self.children.append(new_folder)
        return new_folder

    def add_file(self, name: str, size: int):
        new_file = Node(name, self, size)
        self.children.append(new_file)
        return new_file

    def find_named_child(self, name: str) -> Node | None:
        for child in self.children:
            if child.name == name:
                return child
        return None

    def get_root(self) -> Node:
        if self.parent is None:
            return self
        return self.parent.get_root()

    def get_path(self) -> str:
        if self.parent is None:
            return ""
        return self.parent.get_path() + "/" + self.name

    def get_all_dirs_smaller_than(self, size: int) -> List[Node]:
        dirs = []
        if self.size is None and len(self) <= size:
            dirs.append(self)
        for child in self.children:
            dirs.extend(child.get_all_dirs_smaller_than(size))
        return dirs

    def find_smallest_dir_bigger_than(self, size: int) -> int:
        smallest = 2**31 - 1
        self_len = len(self)
        if self_len < size:
            return smallest

        if size <= self_len < smallest:
            smallest = self_len
        for child in self.children:
            smallest = min(smallest, child.find_smallest_dir_bigger_than(size))
        return smallest

    def __len__(self) -> int:
        if self.size is not None:
            return self.size
        return sum(list(map(len, self.children)))

    def __repr__(self):
        return str(self.size) + " " + self.name if self.size is not None else "dir " + self.name