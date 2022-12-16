from typing import List, Tuple

RIGHT_ORDER = 1
UNDECIDED = 2
WRONG_ORDER = 3


def check_list_order(left: List, right: List) -> int:
    for l, r in zip(left, right):
        order = check_order(l, r)
        if order == WRONG_ORDER:
            return WRONG_ORDER
        elif order == RIGHT_ORDER:
            return RIGHT_ORDER
    if len(left) < len(right):
        return RIGHT_ORDER
    elif len(left) > len(right):
        return WRONG_ORDER
    else:
        return UNDECIDED


def check_int_order(left: int, right: int) -> int:
    if left < right:
        return RIGHT_ORDER
    elif left == right:
        return UNDECIDED
    else:
        return WRONG_ORDER


def check_order(left: List | int, right: List | int) -> int:
    if isinstance(left, int) and isinstance(right, int):
        return check_int_order(left, right)
    if isinstance(left, List) and isinstance(right, List):
        return check_list_order(left, right)
    elif isinstance(left, int):
        return check_order([left], right)
    elif isinstance(right, int):
        return check_order(left, [right])


def main():
    pairs: List[Tuple[List]] = []
    with open("signal.txt", "r") as f:
        signal = f.read().splitlines()
    for i in range(0, len(signal), 3):
        packet_pair = tuple([eval(packet) for packet in signal[i:i+2]])
        pairs.append(packet_pair)

    right_order = []
    for i, pair in enumerate(pairs):
        order_correct = check_order(pair[0], pair[1])
        if order_correct in [RIGHT_ORDER, UNDECIDED]:
            right_order.append(i+1)
    print(sum(right_order))


if __name__ == '__main__':
    main()