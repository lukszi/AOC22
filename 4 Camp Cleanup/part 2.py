from typing import List


def parse_line(line: str) -> List[List[int]]:
    pair_str: List[str] = line.split(",")

    ranges: List[List[int]] = []
    for area_range_str in pair_str:
        area_range = area_range_str.split("-")
        ranges.append([int(x) for x in area_range])

    return ranges


def ranges_overlap(pair_ranges: List[List[int]]) -> bool:
    if pair_ranges[0][0] <= pair_ranges[1][0] <= pair_ranges[0][1]:
        return True
    if pair_ranges[1][0] <= pair_ranges[0][0] <= pair_ranges[1][1]:
        return True
    return False


def main():
    with open("pairs.txt", "r") as file:
        counter: int = 0
        for line in file:
            pair_ranges: List[List[int]] = parse_line(line)
            counter += 1 if ranges_overlap(pair_ranges) else 0
    print(counter)


if __name__ == '__main__':
    main()
