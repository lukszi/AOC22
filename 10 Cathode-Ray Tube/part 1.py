x = [1]

with open("program.txt") as f:
    program = f.read().splitlines()
    for instruction in program:
        if instruction == "noop":
            x.append(x[-1])
        elif instruction.startswith("addx"):
            x.append(x[-1])
            x.append(x[-1] + int(instruction[4:]))

signal_strenghth = sum([x[i-1]*i for i in [20, 60, 100, 140, 180, 220]])
print(signal_strenghth)