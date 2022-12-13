x = [1]

with open("program.txt") as f:
    program = f.read().splitlines()
    for instruction in program:
        if instruction == "noop":
            x.append(x[-1])
        elif instruction.startswith("addx"):
            x.append(x[-1])
            x.append(x[-1] + int(instruction[4:]))

screen = []
for i in range(0, len(x)):
    if i % 40 in [x[i]-1, x[i], x[i]+1]:
        screen.append("#")
    else:
        screen.append(".")

for i in range(0, len(screen), 40):
    print("".join(screen[i:i+40]))
