def parse_line(line):
    pair_str = line.split(",")

    ranges = []
    for area_range_str in pair_str:
        area_range = area_range_str.split("-")
        ranges.append([int(x) for x in area_range])
    
    return ranges


def ranges_contained(pair_ranges):
    if pair_ranges[0][0] <= pair_ranges[1][0] and pair_ranges[0][1] >= pair_ranges[1][1]:
        return True
    if pair_ranges[1][0] <= pair_ranges[0][0] and pair_ranges[1][1] >= pair_ranges[0][1]:
        return True
    return False


with open("pairs.txt", "r") as file:
    counter = 0
    for line in file:
        pair_ranges = parse_line(line)
        counter += 1 if ranges_contained(pair_ranges) else 0

print(counter)
