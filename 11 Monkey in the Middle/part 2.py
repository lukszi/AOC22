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
    return monkey, divider

def parse_monkeys(filename: str):
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
    monkeys = {}
    mod = 1
    for i in range(0, len(lines), 7):
        monkey, divider = parse_monkey(lines[i:i + 6])
        mod *= divider
        monkeys[monkey["name"]] = monkey
    return monkeys, mod


def main():
    monkeys, mod = parse_monkeys("monkeys.txt")
    inspections = run_inspections(monkeys, mod)
    print(inspections)
    values = list(inspections.values())
    max1 = max(values)
    values.remove(max1)
    max2 = max(values)
    monkey_buisnes = max2 * max1
    print(monkey_buisnes)


def run_inspections(monkeys, mod):
    inspections = {monkey["name"]: 0 for monkey in monkeys.values()}
    for _ in range(10000):
        for monkey_i in monkeys.keys():
            monkey = monkeys[monkey_i]
            for item in monkey["items"]:
                # inspect
                new_item = monkey["operation"](item) % mod
                inspections[monkey_i] += 1
                # bored
                if monkey["test"](new_item):
                    monkeys[monkey["true"]]["items"].append(new_item)
                else:
                    monkeys[monkey["false"]]["items"].append(new_item)
            monkey["items"] = []
        if _ in [1, 20, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]:
            print(f"== After round {_} ==")
            for monkey in inspections.keys():
                print(f"Monkey {monkey} inspected items {inspections[monkey]} times.")
    return inspections

if __name__ == '__main__':
    main()
