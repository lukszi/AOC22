from typing import List


def parse_monkey(monkey: List[str]):
    op = monkey[2].split(" = ")[1].split(" ")[1:]
    operator = op[0]
    operand = "x" if op[1] == "old" else int(op[1])
    operation = lambda x: eval(f'x {operator} {operand}')

    divider = int(monkey[3].split("by ")[1])
    test = lambda x: x % divider == 0
    monkey = {
        "name": monkey[0].split(" ")[1][0],
        "items": [int(item) for item in [item.split(",")[0] for item in monkey[1].split(" ")[2:]]],
        "operation": operation,
        "test": test,
        "true": monkey[4].split("monkey ")[1],
        "false": monkey[5].split("monkey ")[1],
    }
    return monkey

def parse_monkeys(filename: str):
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
    monkeys = {}
    for i in range(0, len(lines), 7):
        monkey = parse_monkey(lines[i:i + 6])
        monkeys[monkey["name"]] = monkey
    return monkeys


def main():
    monkeys = parse_monkeys("monkeys.txt")
    inspections = run_inspections(monkeys)
    print(inspections)
    values = list(inspections.values())
    max1 = max(values)
    values.remove(max1)
    max2 = max(values)
    monkey_buisnes = max2 * max1
    print(monkey_buisnes)


def run_inspections(monkeys):
    inspections = {monkey["name"]: 0 for monkey in monkeys.values()}
    for _ in range(20):
        for monkey_i in monkeys.keys():
            print(f"Monkey {monkey_i}:")
            monkey = monkeys[monkey_i]
            for item in monkey["items"]:
                print(f"\tMonkey inspects an item with a worry level of {item}.")
                # inspect
                new_item = monkey["operation"](item)
                print(f"\t\tWorry level is multiplied by {new_item//item} to {new_item}")
                inspections[monkey_i] += 1
                # bored
                new_item //= 3
                print(f"\t\tMonkey gets bored with item. Worry level is divided by 3 to {new_item}")
                if monkey["test"](new_item):
                    monkeys[monkey["true"]]["items"].append(new_item)
                    print(f"\t\Item with worry level {new_item} is thrown to monkey {monkey['true']}")
                else:
                    monkeys[monkey["false"]]["items"].append(new_item)
                    print(f"\t\tItem with worry level {new_item} is thrown to monkey {monkey['false']}")
            monkey["items"] = []
    return inspections


if __name__ == '__main__':
    main()
