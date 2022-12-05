import re
from typing import List, Tuple


def process_starting_state(starting_state: List[str])-> List[List[str]]:
    n_stacks = int(starting_state.pop(-1).split(" ")[-1])
    stacks: List[List[str]] = [[] for _ in range(n_stacks)]

    for line in starting_state:
        for i in range((len(line) + 1) // 4):
            char = line[i * 4 + 1]
            if char != " ":
                stacks[i].append(char)

    [stack.reverse() for stack in stacks]
    return stacks


def process_instructions(cmd_lines: List[str]) -> List[Tuple[int, int, int]]:
    instructions: List[Tuple[int, int, int]] = []
    for cmd_line in cmd_lines:
        matches = re.findall(r"move (\d+) from (\d+) to (\d+)", cmd_line)
        for match in matches:
            instructions.append((int(match[0]), int(match[1])-1, int(match[2])-1))
    return instructions


def parse_file() -> Tuple[List[List[str]], List[Tuple[int, int, int]]]:
    with open("procedure.txt", "r") as f:
        state_lines: List[str] = []
        instruction_lines: List[str] = []
        for line in f:
            if line[0] == "[" or line[0] == " ":
                state_lines.append(line)
            elif line.startswith("move"):
                instruction_lines.append(line)

        starting_state = process_starting_state(state_lines)
        instructions = process_instructions(instruction_lines)
        return starting_state, instructions


def execute_single_instruction(ins: Tuple[int, int, int], state: List[List[str]]):
    n, from_stack, to_stack = ins
    print("Moving {} from {} to {}".format(n, from_stack, to_stack))
    for _ in range(n):
        state[to_stack].append(state[from_stack].pop())

def main():
    state, instructions = parse_file()
    for instruction in instructions:
        execute_single_instruction(instruction, state)
    print("".join([stack[-1] for stack in state]))

if __name__ == "__main__":
    main()

