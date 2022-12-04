with open("rucksacks.txt", "r") as file:
    priority_sum: int = 0
    for line in file:
        # Process line
        line = line.strip()
        i_split = int(len(line) / 2)
        compartments = [line[:i_split], line[i_split:]]

        # Find duplicate
        duplicate: int
        for item in compartments[0]:
            if item in compartments[1]:
                duplicate = ord(item)
                break

        # Fetch priority
        priority: int
        if duplicate in range(ord("a"), ord("z") + 1):
            priority = duplicate - ord("a") + 1
        elif duplicate in range(ord("A"), ord("Z") + 1):
            priority = duplicate - ord("A") + 27

        priority_sum += priority

    print(priority_sum)
