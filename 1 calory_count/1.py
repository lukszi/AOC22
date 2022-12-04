max_cals: int = 0
current_count: int = 0

with open("calories.txt", "r") as file:
    for line in file:
        if line == "\n":
            max_cals = max(max_cals, current_count)
            current_count = 0
        else:
            current_count += (int(line))

print(max_cals)
